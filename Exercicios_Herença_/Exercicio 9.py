# Exercício 9: Herança e Polimorfismo
# Crie uma classe Animal com um método fazer_som(). 
# Em seguida, crie três classes filhas, Cachorro, Gato e Vaca, que sobrescrevem o método fazer_som(). 
# Crie uma lista de animais e itere sobre ela, chamando o método fazer_som() de cada animal.
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        return 'Som de animal'

class Cachorro(Animal):
    def fazer_som(self):
        return 'Au Au'

class Gato(Animal):
    def fazer_som(self):
        return 'Miau Miau'
    
class Vaca(Animal):
   def fazer_som(self):
       return 'Muu Muu'


animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    print(animal.fazer_som())
    

