class Celular:
    def __init__(self, a, b, c, d, e):
        self.marca = a
        self.modelo = b
        self.capacidade = c
        self.SO = d
        self.preço = e

    def __str__(self):
        return f'marca: {self.marca}. Matrícula: {self.modelo}. Capacidade: {self.capacidade}. SO: {self.SO}. preço: {self.preço}\nReferência: {repr(self)}'

celular1 = Celular('Samsung', 'Galaxy S21', '128GB', 'Android', '3500')
celular2 = Celular('Apple', 'iPhone 13', '256GB', 'iOS', '7000')
celular3 = Celular('Xiaomi', 'Redmi Note 11', '128GB', 'Android', '1800')

print(f'{celular1}\n{celular2}\n{celular3}')