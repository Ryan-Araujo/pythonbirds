from unittest import TestCase
from oo.carro import Motor
from oo.carro import Direcao

class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0, motor.velocidade)


    def teste_direcao_inicial(self):
        direcao = Direcao()
        self.assertEqual(direcao.valor , direcao.valor)

    def teste_girar_a_direita(self):
        direcao = Direcao()
        self.assertEqual('Leste',direcao.girar_a_direita_dct[direcao.valor])

    def teste_girar_a_esquerda(self):
        direcao = Direcao()
        self.assertEqual('Oeste',direcao.girar_a_esquerda_dct[direcao.valor])






