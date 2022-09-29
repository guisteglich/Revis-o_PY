"""Crie uma classe Onibus que herda todos métodos e atributos da classe Veiculo abaixo."""


class Veiculo2:
    def __init__(self, nome, max_vel, quilometragem):
        self.nome = nome
        self.max_vel = max_vel
        self.quilometragem = quilometragem

    def get_name(self):
        return self.nome


class Onibus(Veiculo2):
    def __init__(self, nome, max_vel, quilometragem, passageiros, preco_passagem):
        super().__init__(nome, max_vel, quilometragem)
        self.passageiros = passageiros
        self.preco_passagem = preco_passagem

    def get_ticket_price(self):
        return self.preco_passagem

Carro = Veiculo2("Ka", "250", "20000")
Busao = Onibus("Wolks", "180", "10000", 34, 1.56)
print(Carro.get_name())
print(Busao.get_name())
print(Busao.get_ticket_price())