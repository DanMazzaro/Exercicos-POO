class Conta:
    def __init__(self, n, t, s, a, ti):
        self.numero = n
        self.titular = t
        self.saldo = s
        self.agencia = a
        self.tipo_da_conta = ti

conta1 = Conta('01', 'Daniel', 'R$ 1.000.000,00', '11111-1', 'poupança')
conta2 = Conta('02', 'Davidy', 'R$ 1,00', '22222-2', 'corrente')
conta3 = Conta('03', 'Willian', 'R$ -0,01', '33333-3', 'corrente')

print(conta1.numero)
print(conta1.idade)
print(conta1.cpf)
print(conta1.email)
print(conta1.telefone)

print(pessoa2.numero)
print(pessoa2.idade)
print(pessoa2.cpf)
print(pessoa2.email)
print(pessoa2.telefone)

print(pessoa3.numero)
print(pessoa3.idade)
print(pessoa3.cpf)
print(pessoa3.email)
print(pessoa3.telefone)
