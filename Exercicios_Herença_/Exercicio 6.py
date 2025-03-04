# Exercício 6: Uso de super()
# Crie uma classe Pai com um método __init__() que define um atributo nome. 
# Em seguida, crie uma classe Filho que herda de Pai e usa super() para chamar o método __init__() da classe pai 
# e adiciona um atributo idade.

class Pai:
    def __init__(self,nome):
        self.nome = nome


class Filho(Pai):
   def __init__(self, nome, idade):
       super().__init__(nome)
       self.idade = idade

filho = Filho("Carlos", 10)
print(filho.nome)  # Saída: Carlos
print(filho.idade) # Saída: 10