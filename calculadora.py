"""
Calculadora matemática.
Incluye operaciones básicas y avanzadas.
"""

def suma(a, b):
    """Retorna la suma de dos números."""
    return a + b

def resta(a, b):
    """Retorna la resta de dos números."""
    return a - b

def multiplicacion(a, b):
    """Retorna la multiplicación de dos números."""
    return a * b

def division(a, b):
    """Retorna la división de dos números."""
    if b == 0:
        raise ValueError("Valor indeterminado (División por cero)")
    return a / b

def potencia(base, exponente):
    """Calcula una potencia."""
    return base ** exponente

def raiz_cuadrada(a):
    """Calcula la raíz cuadrada."""
    if a < 0:
        raise ValueError(
            "Valor inválido (No se puede calcular la raíz cuadrada de un número negativo)"
        )
    return a ** 0.5

def factorial(n):
    """Calcula el factorial de un número entero."""
    if n < 0:
        raise ValueError("No existe factorial negativo")

    if not isinstance(n, int):
        raise ValueError("El número debe ser un entero")

    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado

if __name__ == "__main__":
    print("3 + 7 =", suma(3, 7))
