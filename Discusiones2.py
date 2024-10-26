import cmath  # Para manejar números complejos

def raices(a: float, b: float, c: float):
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    # Si el discriminante es 0, solo hay una raíz
    if discriminante == 0:
        raiz = (-b + cmath.sqrt(discriminante)) / (2*a)
        return raiz
    
    # Si el discriminante es mayor que 0, hay dos raíces reales
    elif discriminante > 0:
        raiz1 = (-b + discriminante**0.5) / (2*a)
        raiz2 = (-b - discriminante**0.5) / (2*a)
        return raiz1, raiz2

    # Si el discriminante es menor que 0, las raíces son complejas
    else:
        raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2

# Ejemplo de uso
resultado = raices(1.5, -2, 1)
print('La/s raíz/ices de la ecuación cuadrática es/son: ', resultado)
