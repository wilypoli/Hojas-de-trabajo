import math

# Función para calcular arctan con una serie infinita
def arctan(x, terms):
    result = 0
    for n in range(terms):
        term = ((-1)**n) * (x**(2*n + 1)) / (2*n + 1)
        result += term
    return result

# Calcular pi usando la fórmula dada
def calcular_pi(tolerancia):
    pi_real = math.pi
    pi_aprox = 0
    n = 1
    while True:
        pi_aprox = 4 * arctan(1/5, n) - arctan(1/239, n)
        pi_aprox *= 4  # Para ajustar la fórmula pi/4
        if abs(pi_aprox - pi_real) < tolerancia:
            break
        n += 1
    return n

# Ejecutar el cálculo
tolerancia = 10**(-3)
terminos = calcular_pi(tolerancia)
print(f"Número de términos necesarios: {terminos}")
