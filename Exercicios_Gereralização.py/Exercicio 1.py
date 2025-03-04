# A generalização ocorre quando criamos uma classe base (superclasse) que encapsula comportamentos 
# e atributos comuns a várias classes derivadas (subclasses).
# Formas Geométricas
# Crie uma classe base FormaGeometrica com métodos calcular_area() e calcular_perimetro(). 
# Em seguida, crie subclasses como Circulo, Retangulo e Triangulo que herdam de FormaGeometrica e 
# implementam os métodos de acordo com suas fórmulas específicas.

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        ...
    @abstractmethod
    def calcular_perimetro(self):
        ...

class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14 #Better to use 'math.pi'

    def calcular_area(self):
        area_circulo = self.pi * self.raio **2
        return area_circulo
          
    def calcular_perimetro(self):
        Perimetro = 2 * self.pi * self.raio
        return Perimetro

class Retangulo(FormaGeometrica):
    
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
      

    def calcular_area(self):
        area_retangulo = self.largura * self.altura
        return area_retangulo
    
    def calcular_perimetro(self):
        Perimetro = 2 * (self.largura + self.altura )
        return Perimetro    

class Triangulo(FormaGeometrica):

    def __init__(self, base, altura, lado1, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_area(self):
        area_triangulo = (self.base * self.altura)/2
        return area_triangulo
    
    def calcular_perimetro(self):
        Perimetro_triangulo =  self.lado1 + self.lado2 + self.lado3
        return Perimetro_triangulo
        


# Testando
circulo = Circulo(3)
print("Área do Círculo:", circulo.calcular_area())
print("Perímetro do Círculo:", circulo.calcular_perimetro())

retangulo = Retangulo(4, 6)
print("\nÁrea do Retângulo:", retangulo.calcular_area())
print("Perímetro do Retângulo:", retangulo.calcular_perimetro())

triangulo = Triangulo(5, 3, 3, 4, 5)
print("\nÁrea do Triângulo:", triangulo.calcular_area())
print("Perímetro do Triângulo:", triangulo.calcular_perimetro())