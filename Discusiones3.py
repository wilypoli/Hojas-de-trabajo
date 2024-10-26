def calcular_lado_izquierdo(x):
    suma_lado_izquierdo = 0.0
    termino = 1
    denominador = 1.0
    max_terminos = 1000  # Limitar el número máximo de términos para evitar overflow

    while termino <= max_terminos:  # Límite para evitar que el cálculo crezca indefinidamente
        # Calcular el término actual de la serie
        suma_lado_izquierdo += (2.0**(termino - 1) * x**(2*termino - 1)) / denominador
        
        # Calcular el valor del lado derecho
        lado_derecho = (1 + 2*x) / (1 + x + x**2)
        
        # Verificar si la diferencia es menor a la tolerancia
        if abs(suma_lado_izquierdo - lado_derecho) < 1e-6:
            break
        
        # Actualizar el término y el denominador para el siguiente ciclo
        termino += 1
        denominador *= 1 - x**(2*termino)
    
    return termino

# Ejemplo de uso
x = 0.25
terminos_necesarios = calcular_lado_izquierdo(x)
print(f"Se necesitan {terminos_necesarios} términos para alcanzar la precisión deseada.")
