class Celular:
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'

    def fazer_ligacao(self):
        print('Fazendo ligação...')

    def jogar_cobrinha(self):
        print('Jogando cobrinha...')

    def despertador(self):
        print('Pep Pep Pep')

    def calculator(self, v1, v2):
        return v1 + v2

celular = Celular() # Instancia da classe celular

print(celular.marca)

celular.despertador() 
celular.jogar_cobrinha()
result = celular.calculator(1, 1)
print(result)