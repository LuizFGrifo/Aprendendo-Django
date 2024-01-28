from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True) # Campo auto-increment e primary-key
    name = models.CharField(max_length=200) # Campo do tipo char de 200 caracteres

    # Função para retornar os nomes corretamentes, sem ser objeto
    def __str__(self):
        return self.name


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    """" 
    Chave estrangeira da tabela modelo, o segundo parametro
    protege a marca de ser deletada caso aulgum carro esteja 
    usando ela, o terceiro é o nome da relação
    """
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True) # Permite que seja nulo os campos
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.model
    