from typing import List

class Calculation:
    def __init__(self, operand1: float, operand2: float, operator: str, result: float):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator
        self.result = result

    def __str__(self):
        return f"{self.operand1} {self.operator} {self.operand2} = {self.result}"


class Calculator:
    history: List[Calculation] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @classmethod
    def calculate(cls, a: float, b: float, operator: str) -> float:
        if operator == '+':
            result = cls.add(a, b)
        elif operator == '-':
            result = cls.subtract(a, b)
        elif operator == '*':
            result = cls.multiply(a, b)
        elif operator == '/':
            result = cls.divide(a, b)
        else:
            raise ValueError(f"Unsupported operator: {operator}")
        
        # Store in history
        cls.history.append(Calculation(a, b, operator, result))
        return result

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def clear_history(cls):
        cls.history.clear()
