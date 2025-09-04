class Carro:
    def __init__(self, m, ma, a, c, p, e):
        self.__modelo = m
        self.__marca = ma
        self.__ano = a
        self.__cor = c
        self.__placa = p
        self.__estado = e


    def __str__(self):
        return f'modelo: {self.__modelo}\nmarca: {self.__marca}\nano: {self.__ano}\ncor: {self.__cor}\nplaca: {self.__placa}'

    def get__modelo(self):
        return self.__modelo
    def get__marca(self):
        return self.__marca
    def get__ano(self):
        return self.__ano
    def get__cor(self):
        return self.__cor
    def get__placa(self):
        return self.__placa
    
    def set__modelo(self, modelo):
        self.__modelo = modelo 
    def set__modelo(self, marca):
        self.__modelo = marca
    def set__modelo(self, ano):
        self.__modelo = ano
    def set__modelo(self, cor):
        self.__modelo = cor
    def set__modelo(self, placa):
        self.__modelo = placa

    def ligar(self, estado):
        if estado == 'desligado':
            print('o carro esta desligado ')
