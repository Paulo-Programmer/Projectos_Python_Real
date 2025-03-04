# Crie uma classe base Veiculo com atributos como marca, modelo e ano, e métodos como ligar() e desligar(). 
# Depois, crie subclasses como Carro, Moto e Caminhao que herdam de Veiculo e adicionam métodos específicos, 
# como abrir_porta_malas() para Carro.

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        ...

    def desligar(self):
        ...

class Carro(Veiculo):
    ...

class Moto(Veiculo):
    ...

class Caminhao(Veiculo):
    ...
    