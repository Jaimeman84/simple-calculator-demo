from typing import Union, Optional
from abc import ABC, abstractmethod

class Operation(ABC):
    """Abstract base class for calculator operations."""
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass

class Addition(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtraction(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b

class Multiplication(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b

class Division(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

class Calculator:
    """Calculator class that handles basic arithmetic operations."""
    
    def __init__(self):
        self._operations = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division()
        }
    
    def calculate(self, a: Union[int, float], b: Union[int, float], operation: str) -> Optional[float]:
        """
        Perform calculation based on the given operation.
        
        Args:
            a (Union[int, float]): First number
            b (Union[int, float]): Second number
            operation (str): Operation to perform (+, -, *, /)
            
        Returns:
            float: Result of the calculation
            
        Raises:
            ValueError: If operation is invalid or division by zero
        """
        if operation not in self._operations:
            raise ValueError(f"Invalid operation: {operation}")
            
        try:
            return self._operations[operation].execute(float(a), float(b))
        except ValueError as e:
            raise ValueError(str(e)) 