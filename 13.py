"""
Escreva uma classe Retangulo que é inicializada com as propriedades lado e altura, e uma classe Circulo que é inicializada com a propriedade raio.  
Ambas classes devem conter seus métodos area() que retorna a área de cada respectiva figura geométrica. 
Em seguida, crie uma lista de dez objetos contendo objetos aleatórios de ambas classes e faça uma função que calcula a soma das áreas de todos os objetos da lista.
"""

from traceback import print_tb


class Retangulo:
    def __init__(self, lado, altura):
        self.lado = lado
        self.altura = altura

    def area(self):
        return self.lado * self.altura

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

r1 = Retangulo(2, 4)
print(r1.area())
c1 = Circulo(3)
print(c1.area())

