class Pedido:
    def __init__(self, a, b, c, d, e):
        self.numero = a
        self.nome_do_cliente = b
        self.valor_total = c
        self.data = d
        self.status = e


    def __str__(self):
        return f'numero: {self.numero}\nnome do cliente: {self.nome_do_cliente}\nvalor total: {self.valor_total}\ndata: {self.data}\nstatus: {self.status}\nReferência: {repr(self)}'


pedido1 = Pedido('101', 'João Silva', '250.75', '2025-08-15', 'Pago')
pedido2 = Pedido('102', 'Maria Oliveira', '1200.00', '2025-08-14', 'Pendente')
pedido3 = Pedido('103', 'Carlos Santos', '580.40', '2025-08-13', 'Enviado')

print(f'{pedido1}\n{pedido2}\n{pedido3}')
