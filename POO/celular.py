from random import random


class Celular:
    def __init__(self, fabricante, modelo, tela, armazenamento, memoria, camera, bateria, tela_ligada, carga):
        self.fabricante = fabricante
        self.modelo = modelo
        self.tela = tela
        self.armazenamento = armazenamento
        self.memoria = memoria
        self.camera = camera
        self.bateria = bateria
        self.tela_ligada = tela_ligada
        self.carga = carga

    def ligar_tela(self):
        self.tela_ligada = True

    def verificar_carga_bateria(self):
        porcentagem_bateria = random()
        carga_atual = self.bateria * porcentagem_bateria
        bateria_restante = self.bateria - carga_atual

        print(f'Carga atual:{carga_atual:.2f} % - carga restante: {bateria_restante:.2f} mA')


celular_android = Celular("Motorola", "G4", 6, 256, 8, 60, 125, False, 120)
pass

celular_android.ligar_tela()
pass

celular_android.verificar_carga_bateria()
