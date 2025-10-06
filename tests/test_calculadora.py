import pytest
from src.calculadora import sumar, restar, multiplicar, dividir

def test_sumar():
    assert sumar(1, 2) == 3
    assert sumar(-1, 1) == 0

def test_restar():
    assert restar(5, 2) == 3

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)
