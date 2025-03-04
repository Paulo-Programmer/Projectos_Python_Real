# Exercício 7: Classes Abstratas
# Crie uma classe abstrata Animal com um método abstrato fazer_som(). 
# Em seguida, crie duas classes filhas, Cachorro e Gato, que implementam o método fazer_som().
# Dica: Use o módulo abc para criar classes abstratas.
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def fazer_som(self):
        ...

class Cachorro(Animal):
    def fazer_som(self) :
      return 'Au Au'

class Gato(Animal):
    def fazer_som(self):
        return 'Miau Miau'

cachorro = Cachorro()
gato = Gato()

print(cachorro.fazer_som())
print(gato.fazer_som())
