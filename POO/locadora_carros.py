from random import randint
from time import sleep
valor_pedagio_carro = 3.5
valor_pedagio_moto = 2.75

valor_km_rodado_carro = 1.5
valor_km_rodado_moto = 1.0


class Veiculo:
    total_locacoes = 0  # Atributo de classe

    def __init__(self, montadora, modelo, alugado):
        self.montadora = montadora
        self.modelo = modelo
        self.alugado = alugado
        self.valor_fatura = 0
        self.nome_cliente = ""
        print(f'O veiculo {self.montadora}{self.modelo} foi adquirido pela locadora!')

    def alugar_veiculo(self, nome_cliente):
        Veiculo.total_locacoes += 1
        self.alugado = True
        self.nome_cliente = nome_cliente
        # incrementando o numero total de locacoes
        print(f'O veiculo {self.montadora} {self.modelo} foi alugado por {self.nome_cliente}.')

    def devolver_veiculo(self):
        self.alugado = False
        print(f'O veiculo {self.montadora} {self.modelo} foi devolvido por {self.nome_cliente}.')

    def gerar_fatura(self, numero_pedagio, km_rodados):
        raise NotImplementedError


class Carro(Veiculo):  # HERANCA DE VEICULO
    def __init__(self, montadora, modelo, alugado):
        super(Carro, self).__init__(montadora, modelo, alugado)
        print("O  Veiculo adquirido foi um carro")

    def gerar_fatura(self, numero_pedagio, km_rodados):
        self.valor_fatura = (numero_pedagio * valor_pedagio_carro) + (km_rodados * valor_km_rodado_carro)
        print(f'Valor da fatura do carro: {self.valor_fatura}')


class Moto(Veiculo):
    def __init__(self, montadora, modelo, alugado):
        super(Moto, self).__init__(montadora, modelo, alugado)
        print("O  Veiculo adquirido foi uma moto")

    def gerar_fatura(self, numero_pedagio, km_rodados):
        self.valor_fatura = (numero_pedagio * valor_pedagio_moto) + (km_rodados * valor_km_rodado_moto)
        print(f'Valor da fatura do moto: {self.valor_fatura}')


def mostrar_fatura(veiculo):
    print(
        f'O valor da fatura do veiculo {veiculo.montadora}, modelo {veiculo.modelo}, alugado por {veiculo.nome_cliente}'
        f' ficou no valor de R$ {veiculo.valor_fatura}')


# sleep(randint(7, 10))

"""strada = Carro("Fiat", "Freedom", False)
strada.alugar_veiculo("Clécio")
strada.devolver_veiculo()
strada.gerar_fatura(10, 650)
mostrar_fatura(strada)
suzuki_ninja = Moto("Honda", "CB 500", False)
suzuki_ninja.alugar_veiculo("Clécio")
suzuki_ninja.gerar_fatura(10, 854)
mostrar_fatura(suzuki_ninja)
"""
