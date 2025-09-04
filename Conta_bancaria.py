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
print(conta1.titular)
print(conta1.saldo)
print(conta1.agencia)
print(conta1.tipo_da_conta)

print(conta2.numero)
print(conta2.titular)
print(conta2.saldo)
print(conta2.agencia)
print(conta2.tipo_da_conta)

print(conta3.numero)
print(conta3.titular)
print(conta3.saldo)
print(conta3.agencia)
print(conta3.tipo_da_conta)
