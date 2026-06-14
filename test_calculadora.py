"""
Pruebas automatizadas para el módulo calculadora.
Ejecutar con: pytest test_calculadora.py -v
"""

import pytest
from calculadora import suma, resta, multiplicacion, division


def test_suma():
    """Verifica que la suma funcione correctamente."""
    assert suma(5, 3) == 8
    assert suma(0, 0) == 0
    assert suma(-1, 1) == 0


def test_resta():
    """Verifica que la resta funcione correctamente."""
    assert resta(10, 4) == 6
    assert resta(0, 5) == -5
    assert resta(-3, -3) == 0


def test_multiplicacion():
    """Verifica que la multiplicación funcione correctamente."""
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(0, 100) == 0
    assert multiplicacion(-2, 5) == -10


def test_division():
    """Verifica que la división funcione correctamente."""
    assert division(15, 3) == 5.0
    assert division(10, 4) == 2.5


def test_division_por_cero():
    """Verifica que la división por cero lanza una excepción."""
    with pytest.raises(ValueError):
        division(10, 0)
