class Pessoa:
    olhos = 2
    def __init__(self,*filhos, nome, idade = 21):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é  {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):

    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar() #executando a logica da classe pai
        return f'{cumprimentar_da_classe}. Aperto de mão' #sobrescrita de metodo


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    ryan = Mutante(nome='Ryan')
    luciano = Homem(ryan, nome='luciano')
    print(Pessoa.cumprimentar(ryan))
    print(id(ryan))
    print(ryan.cumprimentar())
    print(ryan.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    ryan.sobrenome = 'Araujo'
    print(ryan.sobrenome)
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(ryan.__dict__)
    print(Pessoa.olhos)
    print(Pessoa.olhos)
    print(ryan.olhos)
    print(id(ryan.olhos), id(Pessoa.olhos), id(luciano.olhos))
    print(Pessoa.metodo_estatico())
    print(ryan.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), ryan.nome_e_atributos_de_classe())
    print(ryan.olhos)

    print(luciano.cumprimentar())
    print(ryan.cumprimentar())


