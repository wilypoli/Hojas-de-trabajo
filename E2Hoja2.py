import math

def corte_tres_digitos(valor):
    # Convertir el número a tres dígitos significativos
    return round(valor, 3)

# Suma de 1/i^3 de 1 a 10 (primera serie)
suma1 = 0
for i in range(1, 11):
    valor = 1 / i**3
    suma1 += corte_tres_digitos(valor)

print("Suma de 1 a 10:", corte_tres_digitos(suma1))

# Suma de 1/i^3 de 10 a 1 (segunda serie)
suma2 = 0
for i in range(10, 0, -1):
    valor = 1 / i**3
    suma2 += corte_tres_digitos(valor)

print("Suma de 10 a 1:", corte_tres_digitos(suma2))

# Comparación
if suma1 == suma2:
    print("Ambos métodos son igualmente precisos.")
elif suma1 > suma2:
    print("La suma en el orden de 1 a 10 es más precisa.")
else:
    print("La suma en el orden de 10 a 1 es más precisa.")
