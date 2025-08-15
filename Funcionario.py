class Funcionario:
    def __init__(self, a, b, c, d, e):
        self.nome = a
        self.cargo = b
        self.salario = c
        self.setor = d
        self.data_de_admissao = e

funcionario1 = Funcionario('Davidy', 'CEO', '10.000.000,00', 'Administração', '2025')
funcionario2 = Funcionario('Arthur', 'Escravo', '10 chicotadas dia', 'Geral', '1756')
funcionario2 = Funcionario('Willian', 'Assistente de Escravo', '15 chicotadas hora', 'Geral', '2000')

print(funcionario1.nome)
print(funcionario1.cargo)
print(funcionario1.salario)
print(funcionario1.setor)
print(funcionario1.data_de_admissao)

print(funcionario2.nome)
print(funcionario2.cargo)
print(funcionario2.salario)
print(funcionario2.setor)
print(funcionario2.data_de_admissao)

print(funcionario2.nome)
print(funcionario2.cargo)
print(funcionario2.salario)
print(funcionario2.setor)
print(funcionario2.data_de_admissao)