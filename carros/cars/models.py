from django.db import models

# Criando a tabela carro, onde ela herda de models
class Car(models.Model):
    id = models.AutoField(primary_key=True) # Campo auto-increment e primary-key
    model = models.CharField(max_length=200) # Campo do tipo char de 200 caracteres
    brand = models.CharField(max_length=200) # Campo da Marca do carro
    factory_year = models.IntegerField(blank=True, null=True) # Permite que seja nulo os campos
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
