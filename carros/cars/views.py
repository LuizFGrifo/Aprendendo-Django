from django.shortcuts import render
from cars.models import Car

def cars_views(request):
    cars = Car.objects.all() # Busca todos os carros no BD, por padrão
    search = request.GET.get('search') # Para realizar uma busca por um modelo especifico

    if search: # Verifica se há alguma busca
        cars = cars.filter(model__icontains=search).order_by('model') # Filtra pelo modelo especifico
    
    return render(
            request, 
            'cars.html', 
            {'cars': cars}
        )