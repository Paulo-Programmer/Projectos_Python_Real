# Exercício 3: Herança Multinível
# Crie uma hierarquia de classes com três níveis:
# Pessoa (atributos: nome, idade).
# Funcionario (herda de Pessoa e adiciona salario).
# Gerente (herda de Funcionario e adiciona departamento).

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Funcionaria(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario


class Gerente(Funcionaria):
    def __init__(self, nome, idade, salario, departamento):
        super().__init__(nome, idade, salario)
        self.departamento = departamento


funcionaria = Funcionaria('João António', 25, 3500)
print(f'O funcionario: {funcionaria.nome} tem {funcionaria.idade} recebe R$ {funcionaria.salario}')
print()

gerente = Gerente('Paulo Daniel', 26, 6700, 'TI')
print(f'O gerente {gerente.nome} ganha {gerente.salario} no departamento de {gerente.departamento}')

help(Gerente)
help(gerente)
