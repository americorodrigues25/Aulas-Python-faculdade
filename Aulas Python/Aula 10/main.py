class FiguraGeometrica: 
    def __init__(self, nome):
        self.nome=nome

    def calcula_area(self):
        pass

class Quadrado(FiguraGeometrica):
    def __init__(self, nome, lado):
        super().__init__(nome)
        self.lado = lado

    def calcula_area(self):
        return self.lado**2
    
class Triangulo(FiguraGeometrica):
    def __init__(self, nome, base, altura):
        super().__init__(nome)
        self.base = base
        self.altura = altura

    def calcula_area(self):
        return (self.base * self.altura) /2

class Circulo(FiguraGeometrica):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio 
    
    def calcula_area(self):
        return (3.14 * self.raio)**2
    
quadrado = Quadrado('quadrado', 4)
print(quadrado.calcula_area())

triangulo = Triangulo('Triangulo', 3, 6)
print(triangulo.calcula_area())

circulo = Circulo('Circulo', 35)
print(circulo.calcula_area())