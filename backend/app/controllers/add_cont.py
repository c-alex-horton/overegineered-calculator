from ..services.add_service import Adder

def add_numbers(num1: float, num2: float):
    adder = Adder()
    return {"result": adder.add(num1, num2)}