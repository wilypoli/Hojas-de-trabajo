def sumar_en_orden_inverso(x):
    n = len(x)
    suma = 0
    
    # Sumar desde el último elemento hasta el primero
    for i in range(n-1, -1, -1):
        suma += x[i]
    
    return suma

# Ejemplo de uso
x = [1, 2, 3, 4, 5]
resultado = sumar_en_orden_inverso(x)
print(f"Resultado de la suma en orden inverso: {resultado}")
