# Exercício 4: Sobrescrita de Métodos
# Crie uma classe Forma com um método calcular_area() que retorna 0. 
# Em seguida, crie duas classes filhas, Quadrado e Circulo, 
# que herdam de Forma e sobrescrevem o método calcular_area() para calcular a área correta de cada forma.

class Forma:
    def __init__(self, area):
        self.area = area
    
    def calcular_area(self):
        return 0
    

class Quadrado(Forma):
    def calcular_area(self):
        return float(self.area * self.area)

class Circulo(Forma):
    def calcular_area(self):
        return float(self.area* self.area * 3.14)




lado = int(input('Digite o lado do quadrado: '))
quadrado = Quadrado(lado)
print(f'A area do quadrado com este lado {lado} é : {quadrado.calcular_area()}')

circ = Circulo(3)
print(circ.calcular_area())