import math

# Función para redondear a tres dígitos significativos
def round_three_digits(value):
    if value == 0:
        return 0
    else:
        return round(value, 3 - int(math.floor(math.log10(abs(value)))) - 1)

# Suma con redondeo a tres dígitos para cada término
def suma_con_redondeo():
    suma = 0
    for i in range(1, 11):
        termino = 1 / (i ** 2)
        termino = round_three_digits(termino)  # Redondear a tres dígitos significativos
        suma += termino
        suma = round_three_digits(suma)  # Redondear la suma acumulada a tres dígitos significativos
    return suma

# Realizamos la suma
resultado_suma = suma_con_redondeo()

# Mostramos el resultado
print("Suma con redondeo a tres dígitos:", resultado_suma)
