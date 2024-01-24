''''
Revisando Herança:

Herança, nada mais é do que você herdar os atributos
e funções de uma classe Pai
'''

class Carro():
    numero_rodas = 4 # Propriedades da classe
    quantidade_passageiros = 2

    def acelerar(self):
        print('Vrummmmmm')

    def frear(self):
        print('piiiii')

    def buzinar(self):
        print('fum fum')

class Porsche(Carro): # Herda de carro
    modelo = '992 GT3-RS' # Propriedades da classe
    plataforma = 911
    ano = 2021

porsche = Porsche()
porsche.acelerar()
porsche.buzinar()
    