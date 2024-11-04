from classes import Rectangulo

rectangulo1 = Rectangulo(2, 8)
rectangulo2 = Rectangulo(3, 12)

print("El área del rectángulo 1 es:", rectangulo1.getArea())
print("El área del rectángulo 2 es:", rectangulo2.getArea())

print("El perímetro del rectángulo 1 es:", rectangulo1.getPerimetro())
print("El perímetro del rectángulo 2 es:", rectangulo2.getPerimetro())

resultado = Rectangulo.compararAncho(rectangulo1, rectangulo2)

print("El más ancho es:", resultado)
