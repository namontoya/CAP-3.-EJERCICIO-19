#Capitulo 3. Ejercicio propuesto 19

import math

def calcular_triangulo_equilatero(lado):
    perimetro = 3 * lado
    altura = (math.sqrt(3) / 2) * lado
    area = (math.sqrt(3) / 4) * lado ** 2
    return perimetro, altura, area

lado = float(input("Ingrese la longitud del lado del triángulo equilátero: "))

perimetro, altura, area = calcular_triangulo_equilatero(lado)

print(f"El perímetro del triángulo es: {perimetro}")
print(f"La altura del triángulo es: {altura}")
print(f"El área del triángulo es: {area}")
