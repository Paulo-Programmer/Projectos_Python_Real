# Exercício 8: Herança com Métodos Estáticos
# Crie uma classe Matematica com um método estático somar(a, b). 
# Em seguida, crie uma classe Calculadora que herda de Matematica e adiciona um método estático multiplicar(a, b).

class Matematica:
    @staticmethod
    def somar(a, b):
        soma = a + b
        return soma
    
    @staticmethod
    def multiplicar(a, b):
        multiplicacao = a * b
        return multiplicacao
    
class Calculadora(Matematica):
 
    @staticmethod
    def dividir(a, b):
        try:
            divicao = a/b
            return divicao
        except ZeroDivisionError:
            print('ERRO!!!! UMA DIVISÃO POR 0')
            print(f'você dividiu o {a} por {b}')
    
    @staticmethod
    def resto(a, b):
        resto_div = a % b
        return resto_div

print(Calculadora.dividir(2, 2))
print(Calculadora.somar(4, 9))
print(Calculadora.resto(4, 2))
print(Calculadora.multiplicar(3, 6))

