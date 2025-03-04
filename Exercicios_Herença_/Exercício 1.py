# Exercício 1: Herança Básica
# Crie uma classe chamada Animal com os atributos nome e idade, e um método chamado fazer_som(). 
# Em seguida, crie duas classes filhas, Cachorro e Gato, que herdam de Animal e sobrescrevem o método fazer_som() para retornar "Au Au!" 
# e "Miau!", respectivamente.

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_som(self):
        print(f'O {self.nome} faz o som')


class Cachorro(Animal):
    def fazer_som(self):
        print(f'O {self.nome} de {self.idade} faz Au Au')

class Gato(Animal):
    def fazer_som(self):
        print(f'O {self.nome} de {self.idade} faz Miau!')


cachorro1 = Cachorro('Pitbull', 3)
cachorro1.fazer_som()
cachorro2 = Cachorro('Pastor Alemão', 4)
cachorro2.fazer_som()

gato1 = Gato('Titirica', 2)
gato1.fazer_som()
gato2 = Gato('Ttt', 3)
gato2.fazer_som()

help(Animal)
help(Cachorro)
help(Gato)
