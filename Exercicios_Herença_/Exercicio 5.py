# Exercício 5: Herança Múltipla
# Crie uma classe Eletronico com o atributo voltagem e uma classe Smart com o atributo conectado_internet. 
# Em seguida, crie uma classe Smartphone que herda de ambas as classes e adiciona o atributo tela.

class Eletronico:
    def __init__(self, voltagem):
        self.voltagem = voltagem


class Smart:
    def __init__(self, conectado_internet):
        self.conectado_internet = conectado_internet

class Smartphone(Eletronico, Smart):
    def __init__(self, voltagem,conectado_internet, tela):
        super().__init__(voltagem)
        self.conectado_internet = conectado_internet
        self.tela = tela

smartphone = Smartphone(220, True, 6.1)
print(smartphone.voltagem)           # Saída: 220
print(smartphone.conectado_internet) # Saída: True
print(smartphone.tela)               # Saída: 6.1

help(Smartphone)
        