def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Valor indeterminado (División por cero)")
    return a / b

def pow(base, exponente):
    return base ** exponente

def sqrt(a):
    if a < 0:
        raise ValueError('Valor inválido (No se puede calcular la raíz cuadrada de un número negativo)')
    return a ** 0.5

def root(numero, indice):
    if indice == 0:
        raise ValueError("Valor inválido (El índice no puede ser cero)")
    return numero ** (1 / indice)

def fact(n):
    if n < 0:
        raise ValueError("No existe factorial negativo")
    if not isinstance(n, int):
        raise ValueError("El número debe ser un entero")

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado