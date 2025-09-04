class Aluno:
    def __init__(self, a, b, c, d, e):
        self.nome = a
        self.matricula = b
        self.nota = c
        self.curso = d
        self.email = e

    def __str__(self):
        return f'Nome: {self.nome}. Matrícula: {self.matricula}. Nota: {self.nota}. Curso: {self.curso}. Email: {self.email}\nReferência: {repr(self)}'

aluno1 = Aluno('Daniel', 'ABC111', '10', 'Cooperativismo', 'danielmazzaro44@gmail.com')
aluno2 = Aluno('Davidy', 'DEF222', '7', 'Informatica', 'davidy.klein632@gmail.com')
aluno3 = Aluno('Wilian', 'GHI333', '0,4', 'Agronomia', 'willianbortolato73@gmail.com')

print(f'{aluno1}\n{aluno2}\n{aluno3}')