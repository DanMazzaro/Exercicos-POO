class Pessoa:
    def __init__(self, a, b, c, d, e):
        self.nome = a
        self.idade = b
        self.cpf = c
        self.email = d
        self.telefone = e

pessoa1 = Pessoa('Daniel', '16', '111.111.111.11', 'danielmazzaro44@gmail.com', '46 99900-9835')
pessoa2 = Pessoa('Davidy', '16', '222.222.222.22', 'davidy.klein632@gmail.com', '46 99977-7618')
pessoa3 = Pessoa('Wilian', '16', '333.333.333.33', 'willianbortolato73@gmail.com', '46 98833-0863')

print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.cpf)
print(pessoa1.email)
print(pessoa1.telefone)

print(pessoa2.nome)
print(pessoa2.idade)
print(pessoa2.cpf)
print(pessoa2.email)
print(pessoa2.telefone)

print(pessoa3.nome)
print(pessoa3.idade)
print(pessoa3.cpf)
print(pessoa3.email)
print(pessoa3.telefone)
