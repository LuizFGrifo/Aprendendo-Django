"""
Local onde vamos concentrar todas as forms
do new_car.html
"""
from django import forms
from cars.models import Brand, Car


# Forma mais verbosa de criar formularios
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) # Lista todos os objetos da tabela Brand
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
    
# Forma menos verbosa e mais facil de fazer
class CarModelForm(forms.ModelForm):
    class Meta: # Sobrescreve a class meta
        model = Car # Indica que o model é da tabela Car
        fields = '__all__' # Puxa todos os campos da tabela Car

