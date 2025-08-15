class Livro:
    def __init__(self, t, a, n, e, an):
        self.titulo = t
        self.autor = a
        self.numero_de_paginas = n
        self.editora = e
        self.ano_de_publicacao = an


livro1 = Livro('Harry Poter', 'Alfredo', '650', 'Céu Azul', '1986')
livro2 = Livro('O jogo da Vida', 'Carlos', '278', 'Papiro', '2013')
livro3 = Livro('Senhor dos Aneis', 'Julio', '754', 'Cruz', '1990')


print(livro1.titulo)
print(livro1.autor)
print(livro1.numero_de_paginas)
print(livro1.editora)
print(livro1.ano_de_publicacao)

print(livro2.titulo)
print(livro2.autor)
print(livro2.numero_de_paginas)
print(livro2.editora)
print(livro2.ano_de_publicacao)

print(livro3.titulo)
print(livro3.autor)
print(livro3.numero_de_paginas)
print(livro3.editora)
print(livro3.ano_de_publicacao)

