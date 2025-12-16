"""
Тесты для модуля calculator.py
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import add, subtract, multiply, divide, power

def test_add():
    """Тест функции сложения"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 2.5) == 5.0

def test_subtract():
    """Тест функции вычитания"""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(10, 10) == 0

def test_multiply():
    """Тест функции умножения"""
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(2.5, 2) == 5.0

def test_divide():
    """Тест функции деления"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5
    
    # Тест на исключение при делении на ноль
    try:
        divide(10, 0)
        assert False, "Должно было возникнуть исключение"
    except ValueError as e:
        assert str(e) == "Деление на ноль невозможно"

def test_power():
    """Тест функции возведения в степень"""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 2) == 9
    assert power(4, 0.5) == 2

def test_all_operations():
    """Комплексный тест всех операций"""
    assert add(subtract(10, 5), multiply(2, 3)) == 11
    assert divide(multiply(4, 6), 2) == 12
    assert power(add(1, 1), 3) == 8