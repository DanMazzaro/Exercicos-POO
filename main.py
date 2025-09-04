from Aluno import Aluno
from Carro import Carro
from Celular import Celular
from Conta_bancaria import Conta
from Filme import Filme
from Funcionario import Funcionario
from Livro import Livro
from Pedido import Pedido
from Pessoa import Pessoa
from Produto import Produto


print('menu de atividades: \natividade 1 Carro \natividade 2 Livro \natividade 3 Pessoa \natividade 4 Conta Bancaria \natividade 5 Produto \natividade 6 Aluno \natividade 7 Filme \natividade 8 Funcionario \natividade 9 Celular \natividade 10 Pedido')

atividade = input('qual atividade voce quer acessar? digite de 1 a 10: ')

while True:
    if atividade == '1':
        print('voce abriu a atividade 1 Carro')
        modelo = Carro(input('qual o modelo do carro?'))
        marca = Carro(input('qual a marca do carro?'))
        ano = Carro(input('qual o ano do carro?'))
        cor = Carro(input('qual a cor do carro?'))
        placa = Carro(input('qual a placa do carro?'))
