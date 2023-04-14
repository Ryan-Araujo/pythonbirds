from unittest import TestCase
from oo.pessoa import Mutante

class PessoaTestCase(TestCase):
    def test_olhos(self):
        pessoa = Mutante(nome='ryan')
        self.assertEqual(3 ,pessoa.olhos)