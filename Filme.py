class Filme:
    def __init__(self, a, b, c, d, e):
        self.titulo = a
        self.diretor = b
        self.duracao = c
        self.genero = d
        self.ano = e

filme1 = Filme('Circulo de Fogo', 'Mark Zuckeibht', '02:36', 'Ficção Científica', '2008')
filme2 = Filme('Truque de Mestre', 'Alakazan', '1:54', 'Ação', '2017')
filme3 = Filme('Todo Mundo Em Pânico', 'Frederico Chocota', '2:20', 'Comédia', '2002')

print(filme1.titulo)
print(filme1.diretor)
print(filme1.duracao)
print(filme1.genero)
print(filme1.ano)

print(filme2.titulo)
print(filme2.diretor)
print(filme2.duracao)
print(filme2.genero)
print(filme2.ano)

print(filme3.titulo)
print(filme3.diretor)
print(filme3.duracao)
print(filme3.genero)
print(filme3.ano)