''''
Revisando Polimorfismo:

Polimorfismo, nada mais é do que classes difrentes que herdam
de uma mesma classe Pai. Ela permite ter propriedades e métodos 
com o mesmo nome, que executam coisas diferentes, herdando da mesma classe.
'''

class Animal():

    def emitir_som(self):
        print('Qualquer som...')

class Cachorro(Animal):
    def emitir_som(self): # Polimorfismo, estou sobrescrevendo a função de Animal
        print('Au Au')

class Gato(Animal):
    def emitir_som(self):
        print('Miau')

cachorro = Cachorro()
gato = Gato()
cachorro.emitir_som()
gato.emitir_som()