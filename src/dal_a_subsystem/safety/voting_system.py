"""
2-out-of-3 (2oo3) Voting System for DAL-A Software Subsystem
============================================================

Implements redundant voting system for fault tolerance in safety-critical applications.
Provides Byzantine fault tolerance and graceful degradation on component failures.

DO-178C Objectives:
- A-8: Software verification procedures are correct and complete
- A-9: Software verification procedures conform to software requirements

Safety Requirements:
- SRS-VOTE-001: 2oo3 voting for all safety-critical decisions
- SRS-VOTE-002: Byzantine fault tolerance up to 1 failure
- SRS-VOTE-003: Automatic voter health monitoring
- SRS-VOTE-004: Graceful degradation to 1oo2 on voter failure
"""

import time
import logging
from typing import Any, List, Callable, Optional, Dict, Tuple
from dataclasses import dataclass
from enum import Enum
import threading
import hashlib


class VoterState(Enum):
    """Voter component states"""
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    FAILED = "FAILED"
    OFFLINE = "OFFLINE"


class VotingResult(Enum):
    """Voting decision outcomes"""
    CONSENSUS = "CONSENSUS"          # All voters agree
    MAJORITY = "MAJORITY"            # 2/3 voters agree
    NO_CONSENSUS = "NO_CONSENSUS"    # No majority agreement
    INSUFFICIENT_VOTERS = "INSUFFICIENT_VOTERS"  # <2 healthy voters


@dataclass
class VoterComponent:
    """Individual voter component in the 2oo3 system"""
    name: str
    compute_function: Callable[..., Any]
    state: VoterState = VoterState.HEALTHY
    last_result: Any = None
    last_execution_time: float = 0.0
    error_count: int = 0
    total_votes: int = 0
    
    def execute(self, *args, **kwargs) -> Tuple[Any, bool]:
        """
        Execute voter computation and return result with success flag
        
        Returns:
            Tuple[result, success]: Computation result and success status
        """
        try:
            start_time = time.time()
            result = self.compute_function(*args, **kwargs)
            
            self.last_result = result
            self.last_execution_time = time.time() - start_time
            self.total_votes += 1
            
            return result, True
            
        except Exception as e:
            logging.error(f"Voter {self.name} execution failed: {e}")
            self.error_count += 1
            
            # Update voter state based on error rate
            error_rate = self.error_count / max(1, self.total_votes)
            if error_rate > 0.1:  # >10% error rate
                self.state = VoterState.FAILED
            elif error_rate > 0.05:  # >5% error rate
                self.state = VoterState.DEGRADED
                
            return None, False


class TwoOfThreeVoting:
    """
    2-out-of-3 Voting System for Safety-Critical Applications
    
    Implements Byzantine fault-tolerant voting with graceful degradation.
    Provides redundancy for safety-critical computations and decisions.
    """
    
    def __init__(self, name: str, comparison_tolerance: float = 1e-6):
        """
        Initialize 2oo3 voting system
        
        Args:
            name: Name identifier for this voting system
            comparison_tolerance: Tolerance for numerical comparisons
        """
        self.name = name
        self.comparison_tolerance = comparison_tolerance
        self.voters: List[VoterComponent] = []
        
        # Voting statistics
        self.total_votes = 0
        self.consensus_votes = 0
        self.majority_votes = 0
        self.failed_votes = 0
        
        # Health monitoring
        self.health_check_interval = 1.0  # seconds
        self.last_health_check = 0.0
        self.system_health = 100.0
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def add_voter(self, name: str, compute_function: Callable) -> bool:
        """
        Add a voter component to the system
        
        Args:
            name: Voter identifier
            compute_function: Function that performs the computation
            
        Returns:
            bool: True if voter added successfully
            
        Implements: SRS-VOTE-001 (2oo3 voting setup)
        """
        if len(self.voters) >= 3:
            self.logger.error("Cannot add more than 3 voters to 2oo3 system")
            return False
            
        if any(voter.name == name for voter in self.voters):
            self.logger.error(f"Voter {name} already exists")
            return False
            
        voter = VoterComponent(name, compute_function)
        self.voters.append(voter)
        
        self.logger.info(f"Added voter {name} to {self.name} voting system")
        return True
    
    def vote(self, *args, **kwargs) -> Tuple[Any, VotingResult, Dict]:
        """
        Perform 2oo3 voting on the given inputs
        
        Args:
            *args, **kwargs: Arguments to pass to voter functions
            
        Returns:
            Tuple[result, voting_result, details]: 
                - result: The voted result (None if no consensus)
                - voting_result: VotingResult enum indicating outcome
                - details: Dict with voting details and metrics
                
        Implements: SRS-VOTE-002 (Byzantine fault tolerance)
        """
        self.total_votes += 1
        vote_start_time = time.time()
        
        # Get healthy voters
        healthy_voters = [v for v in self.voters if v.state in [VoterState.HEALTHY, VoterState.DEGRADED]]
        
        if len(healthy_voters) < 2:
            self.failed_votes += 1
            self.logger.critical(f"Insufficient healthy voters: {len(healthy_voters)}/3")
            return None, VotingResult.INSUFFICIENT_VOTERS, self._get_vote_details([], vote_start_time)
        
        # Execute voting
        results = []
        for voter in healthy_voters:
            result, success = voter.execute(*args, **kwargs)
            if success:
                results.append((voter.name, result))
        
        # Analyze voting results
        voting_result, final_result = self._analyze_votes(results)
        
        # Update statistics
        if voting_result == VotingResult.CONSENSUS:
            self.consensus_votes += 1
        elif voting_result == VotingResult.MAJORITY:
            self.majority_votes += 1
        else:
            self.failed_votes += 1
        
        # Perform health check
        self._perform_health_check()
        
        vote_details = self._get_vote_details(results, vote_start_time)
        
        self.logger.info(f"Vote completed: {voting_result.value}, "
                        f"Result: {final_result}, "
                        f"Healthy voters: {len(healthy_voters)}/3")
        
        return final_result, voting_result, vote_details
    
    def _analyze_votes(self, results: List[Tuple[str, Any]]) -> Tuple[VotingResult, Any]:
        """
        Analyze voting results to determine consensus
        
        Implements: SRS-VOTE-002 (Byzantine fault tolerance)
        """
        if len(results) < 2:
            return VotingResult.INSUFFICIENT_VOTERS, None
        
        # Group similar results
        result_groups = {}
        for voter_name, result in results:
            # Create a hash key for grouping similar results
            result_key = self._create_result_key(result)
            
            if result_key not in result_groups:
                result_groups[result_key] = []
            result_groups[result_key].append((voter_name, result))
        
        # Find majority
        max_group_size = max(len(group) for group in result_groups.values())
        majority_groups = [group for group in result_groups.values() if len(group) == max_group_size]
        
        if len(majority_groups) == 1 and max_group_size >= 2:
            # We have a clear majority (2 or 3 voters agree)
            majority_group = majority_groups[0]
            result = majority_group[0][1]  # Take the result from the first voter in the group
            
            if max_group_size == len(results):
                return VotingResult.CONSENSUS, result
            else:
                return VotingResult.MAJORITY, result
        else:
            # No clear majority
            return VotingResult.NO_CONSENSUS, None
    
    def _create_result_key(self, result: Any) -> str:
        """Create a hash key for result comparison"""
        try:
            if isinstance(result, (int, float)):
                # For numerical results, group within tolerance
                normalized = round(result / self.comparison_tolerance) * self.comparison_tolerance
                return f"num_{normalized}"
            elif isinstance(result, str):
                return f"str_{result}"
            elif isinstance(result, bool):
                return f"bool_{result}"
            else:
                # For complex objects, use string representation
                return f"obj_{str(result)}"
        except:
            return f"unknown_{id(result)}"
    
    def _perform_health_check(self) -> None:
        """
        Perform system health monitoring
        
        Implements: SRS-VOTE-003 (Health monitoring)
        """
        current_time = time.time()
        if current_time - self.last_health_check < self.health_check_interval:
            return
        
        self.last_health_check = current_time
        
        # Calculate system health metrics
        healthy_voters = sum(1 for v in self.voters if v.state == VoterState.HEALTHY)
        degraded_voters = sum(1 for v in self.voters if v.state == VoterState.DEGRADED)
        failed_voters = sum(1 for v in self.voters if v.state == VoterState.FAILED)
        
        # Health score calculation
        health_score = (healthy_voters * 100 + degraded_voters * 50) / len(self.voters)
        self.system_health = health_score
        
        # Log health status
        if health_score < 67:  # Less than 2/3 healthy
            self.logger.warning(f"Voting system {self.name} health degraded: {health_score:.1f}%")
        
        # Check for degradation to 1oo2 mode
        if failed_voters >= 1:
            self.logger.warning(f"Voting system {self.name} operating in degraded mode: "
                              f"{healthy_voters + degraded_voters}/3 voters available")
    
    def _get_vote_details(self, results: List[Tuple[str, Any]], start_time: float) -> Dict:
        """Get detailed voting information for monitoring"""
        vote_duration = time.time() - start_time
        
        return {
            "timestamp": time.time(),
            "vote_duration_ms": vote_duration * 1000,
            "total_voters": len(self.voters),
            "participating_voters": len(results),
            "results": {voter_name: str(result) for voter_name, result in results},
            "voter_states": {v.name: v.state.value for v in self.voters},
            "system_health_percent": self.system_health,
            "statistics": {
                "total_votes": self.total_votes,
                "consensus_votes": self.consensus_votes,
                "majority_votes": self.majority_votes,
                "failed_votes": self.failed_votes,
                "consensus_rate": self.consensus_votes / max(1, self.total_votes) * 100,
                "success_rate": (self.consensus_votes + self.majority_votes) / max(1, self.total_votes) * 100
            }
        }
    
    def get_system_status(self) -> Dict:
        """
        Get comprehensive system status
        
        Returns:
            Dict containing system health and performance metrics
        """
        return {
            "name": self.name,
            "timestamp": time.time(),
            "system_health_percent": self.system_health,
            "voters": {
                voter.name: {
                    "state": voter.state.value,
                    "error_count": voter.error_count,
                    "total_votes": voter.total_votes,
                    "error_rate_percent": (voter.error_count / max(1, voter.total_votes)) * 100,
                    "last_execution_time_ms": voter.last_execution_time * 1000,
                    "last_result": str(voter.last_result) if voter.last_result is not None else None
                } for voter in self.voters
            },
            "statistics": {
                "total_votes": self.total_votes,
                "consensus_votes": self.consensus_votes,
                "majority_votes": self.majority_votes,
                "failed_votes": self.failed_votes,
                "consensus_rate_percent": (self.consensus_votes / max(1, self.total_votes)) * 100,
                "majority_rate_percent": (self.majority_votes / max(1, self.total_votes)) * 100,
                "success_rate_percent": ((self.consensus_votes + self.majority_votes) / max(1, self.total_votes)) * 100
            },
            "fault_tolerance": {
                "healthy_voters": sum(1 for v in self.voters if v.state == VoterState.HEALTHY),
                "degraded_voters": sum(1 for v in self.voters if v.state == VoterState.DEGRADED),
                "failed_voters": sum(1 for v in self.voters if v.state == VoterState.FAILED),
                "byzantine_tolerance": len([v for v in self.voters if v.state in [VoterState.HEALTHY, VoterState.DEGRADED]]) >= 2,
                "operational_mode": "2oo3" if len([v for v in self.voters if v.state == VoterState.HEALTHY]) >= 2 else "1oo2"
            }
        }
    
    def reset_voter(self, voter_name: str) -> bool:
        """
        Reset a failed voter component
        
        Implements: SRS-VOTE-004 (Graceful degradation)
        """
        for voter in self.voters:
            if voter.name == voter_name:
                voter.state = VoterState.HEALTHY
                voter.error_count = 0
                self.logger.info(f"Reset voter {voter_name}")
                return True
        return False
    
    def remove_voter(self, voter_name: str) -> bool:
        """Remove a voter from the system"""
        for i, voter in enumerate(self.voters):
            if voter.name == voter_name:
                del self.voters[i]
                self.logger.info(f"Removed voter {voter_name}")
                return True
        return False