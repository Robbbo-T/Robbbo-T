# physics_solvers/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple, Callable
import subprocess
import json
import os
import shlex
try:
    from ..core.types import SolverError, SolverTimeoutError
except ImportError:
    import sys
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    sys.path.insert(0, parent_dir)
    from core.types import SolverError, SolverTimeoutError

class PhysicsSolverInterface(ABC):
    """Base interface for external physics solvers"""
    
    @abstractmethod
    def validate(self, requirement: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        pass

    @abstractmethod
    def compute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        pass

class ExternalSolverAdapter:
    """
    Adapter for external solvers (OpenFOAM, CalculiX, etc.)
    Command building and parsing are injected so this stays generic.
    """
    
    def __init__(
        self,
        solver_config: Dict[str, Any],
        command_builder: Callable[[str, str], list],
        result_parser: Callable[[str, str], Dict[str, Any]],
        workdir: str = "work"
    ):
        self.solver_type = solver_config['type']
        self.executable = solver_config['executable']
        self.template_dir = solver_config['templates']
        self.timeout = solver_config.get('timeout', 300)
        self.command_builder = command_builder
        self.result_parser = result_parser
        self.workdir = workdir
        os.makedirs(self.workdir, exist_ok=True)

    def run_solver(self, case_path: str, case_name: str = "case") -> Dict[str, Any]:
        """Execute external solver with error handling"""
        cmd = self.command_builder(self.executable, case_path)
        
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=case_path if os.path.isdir(case_path) else self.workdir
            )
            
            # Persist logs for traceability
            log_dir = os.path.join(self.workdir, f"{case_name}_logs")
            os.makedirs(log_dir, exist_ok=True)
            
            with open(os.path.join(log_dir, "stdout.log"), "w") as f:
                f.write(proc.stdout or "")
            with open(os.path.join(log_dir, "stderr.log"), "w") as f:
                f.write(proc.stderr or "")

            if proc.returncode != 0:
                raise SolverError(
                    self.solver_type, 
                    case_path, 
                    proc.stderr, 
                    proc.returncode
                )

            return self.result_parser(case_path, proc.stdout)

        except subprocess.TimeoutExpired:
            raise SolverTimeoutError(self.solver_type, self.timeout, case_path)