class Pessoa:
    olhos = 2
    def __init__(self,*filhos, nome, idade = 21):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    ryan = Pessoa(nome='Ryan')
    luciano = Pessoa(ryan, nome='luciano')
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
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(ryan.olhos)
    print(id(ryan.olhos), id(Pessoa.olhos), id(luciano.olhos))

