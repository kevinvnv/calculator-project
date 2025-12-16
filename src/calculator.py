"""
Простой калькулятор для практической работы
"""

def add(a: float, b: float) -> float:
    """Сложение двух чисел"""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитание второго числа из первого"""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножение двух чисел"""
    return a * b

def divide(a: float, b: float) -> float:
    """Деление первого числа на второе"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def power(a: float, b: float) -> float:
    """Возведение в степень"""
    return a ** b