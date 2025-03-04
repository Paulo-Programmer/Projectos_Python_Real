# Exercício 2: Herança com Atributos Adicionais
# Crie uma classe Veiculo com os atributos marca e modelo. 
# Em seguida, crie duas classes filhas, Carro e Moto, que herdam de Veiculo e adicionam um atributo específico: 
# portas para Carro e cilindradas para Moto.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
       


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas
        

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas


carro = Carro('Fiat', 'Sedan A', 4)
moto = Moto('Tesk', 'Tesk a', 450)

print(carro.marca, carro.modelo)
print(f'Portas: {carro.portas}')
print(moto.marca, moto.modelo)
print(f'A cilindrada: {moto.cilindradas}')

