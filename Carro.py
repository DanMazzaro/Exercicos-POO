class Carro:
    def __init__(self, m, ma, a, c, p):
        self.modelo = m
        self.marca = ma
        self.ano = a
        self.cor = c
        self.placa = p

carro1 = Carro('GTR R34', 'Nissan', '2008', 'Azul', 'ABC 111')
carro2 = Carro('Eclipse', 'Mitsubishi', '2009', 'Verde', 'DEF 222')
carro3 = Carro('Supra', 'Toyota', '2007', 'Laranja', 'GHI 333')

print(carro1.modelo)
print(carro1.marca)
print(carro1.ano)
print(carro1.cor)
print(carro1.placa)

print(carro2.modelo)
print(carro2.marca)
print(carro2.ano)
print(carro2.cor)
print(carro2.placa)

print(carro3.modelo)
print(carro3.marca)
print(carro3.ano)
print(carro3.cor)
print(carro3.placa)

