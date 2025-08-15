class Produto:
    def __init__(self, a, b, c, d, e):
        self.nome = a
        self.preço = b
        self.quantidade_em_estoque = c
        self.codigo = d
        self.fornecedor = e

produto1 = Produto('Leite', 'R$ 4,59', '500', '111 111', 'Tirol')
produto2 = Produto('Café', 'R$ 20,50', '300', '222 222', 'Melita')
produto3 = Produto('Pão Fatiado ', 'R$ 7,00', '450', '333 333', 'Pullman')

print(produto1.nome)
print(produto1.preço)
print(produto1.quantidade_em_estoque)
print(produto1.codigo)
print(produto1.fornecedor)

print(produto2.nome)
print(produto2.preço)
print(produto2.quantidade_em_estoque)
print(produto2.codigo)
print(produto2.fornecedor)

print(produto3.nome)
print(produto3.preço)
print(produto3.quantidade_em_estoque)
print(produto3.codigo)
print(produto3.fornecedor)