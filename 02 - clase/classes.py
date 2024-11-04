class Rectangulo(object):
    def __init__(self, largo, ancho):
        self._ancho = ancho
        self._largo = largo

    def getArea(self):
        return self._ancho * self._largo
    
    def getPerimetro(self):
        return 2 * (self._ancho + self._largo)

    def getAncho(self):
        return self._ancho

    def compararAncho(rectangulo1, rectangulo2):
        if rectangulo1.getAncho() > rectangulo2.getAncho():
            return "El rectángulo 1 es más ancho"
        elif rectangulo1.getAncho() < rectangulo2.getAncho():
            return "El rectángulo 2 es más ancho"
        else:
            return "Tienen el mismo ancho"

