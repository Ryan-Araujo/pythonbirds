NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class Direcao:
    girar_a_direita = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    girar_a_esquerda = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor == NORTE

    def girar_a_direita(self):
        self.valor = self.girar_a_direita[self.valor]
    def girar_a_esquerda(self):
        self.valor = self.girar_a_esquerda[self.valor]






