# Exercício 10: Herança e Composição
# Crie uma classe Motor com um atributo potencia. 
# Em seguida, crie uma classe Carro que contém uma instância de Motor como atributo. 
# Adicione um método descrever() que exibe a potência do motor.

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Rodas:
    def __init__(self, rodas):
        self.rodas = rodas

class Carro():
    def __init__(self, potencia, rodas):
        self.motor = Motor(potencia)
        self.rodas = Rodas(rodas)

    
    def descrever(self):
        print(f'O Carro com {self.motor.potencia} de cavalos e {self.rodas.rodas} rodas!! ')


carro = Carro(150, 4)
carro.descrever()