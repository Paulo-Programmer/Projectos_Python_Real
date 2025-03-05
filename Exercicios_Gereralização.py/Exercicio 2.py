# Crie uma classe base Veiculo com atributos como marca, modelo e ano, e métodos como ligar() e desligar(). 
# Depois, crie subclasses como Carro, Moto e Caminhao que herdam de Veiculo e adicionam métodos específicos, 
# como abrir_porta_malas() para Carro.

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano
    
    def ligar(self):
        print(f'{self.marca} {self.modelo} está ligado.')

    def desligar(self):
        print(f'{self.marca} {self.modelo} está desligado.')

class Carro(Veiculo):
    
    def abrir_portas(self):
        print(f'As portas do {self.marca} {self.modelo}')

class Moto(Veiculo):
    def empinar(self):
        print(f'A moto {self.marca} {self.modelo} está empinando!')
    

class Caminhao(Veiculo):
    def carregar_carga(self):
        print(f'O caminhão {self.marca} {self.modelo} está sendo carregado.')

carro = Carro('Toyota', 'Corolla', 2023)
carro.ligar()
carro.abrir_portas()

moto = Moto('Honda', 'CB 500', 2022)
moto.ligar()
moto.empinar()


caminhao = Caminhao('Volvo', 'FH 540', 2021)
caminhao.ligar()
caminhao.carregar_carga()
