from abc import ABC, abstractmethod
from typing import Dict, Any, Tuple, Callable
import subprocess
import os

class PhysicsSolverInterface(ABC):
    @abstractmethod
    def validate(self, requirement: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        pass

    @abstractmethod
    def compute(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        pass

class ExternalSolverAdapter:
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
        cmd = self.command_builder(self.executable, case_path)
        
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=case_path if os.path.isdir(case_path) else self.workdir
            )
            
            log_dir = os.path.join(self.workdir, f"{case_name}_logs")
            os.makedirs(log_dir, exist_ok=True)
            
            with open(os.path.join(log_dir, "stdout.log"), "w") as f:
                f.write(proc.stdout or "")
            with open(os.path.join(log_dir, "stderr.log"), "w") as f:
                f.write(proc.stderr or "")

            if proc.returncode != 0:
                from core.types import SolverError
                raise SolverError(
                    self.solver_type, 
                    case_path, 
                    proc.stderr, 
                    proc.returncode
                )

            return self.result_parser(case_path, proc.stdout)

        except subprocess.TimeoutExpired:
            from core.types import SolverTimeoutError
            raise SolverTimeoutError(self.solver_type, self.timeout, case_path)