from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View


def cars_views(request):
    cars = Car.objects.all()  # Busca todos os carros no BD, por padrão
    search = request.GET.get('search')  # Para realizar uma busca por um modelo especifico

    if search:  # Verifica se há alguma busca
        cars = cars.filter(model__icontains=search).order_by('model')  # Filtra pelo modelo especifico

    return render(
        request,
        'cars.html',
        {'cars': cars}
    )


# Modelo Class Based Views (CBVs)
class CarsView(View):
    def get(self, request):
        cars = Car.objects.all()  # Busca todos os carros no BD, por padrão
        search = request.GET.get('search')  # Para realizar uma busca por um modelo especifico

        if search:  # Verifica se há alguma busca
            cars = cars.filter(model__icontains=search).order_by('model')  # Filtra pelo modelo especifico

        return render(
            request,
            'cars.html',
            {'cars': cars}
        )


def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():  # Verifica se os formularios são validos
            new_car_form.save()  # Salva os dados
            return redirect('cars_list')  # Retorna para a pagina de lista de carros
    else:
        new_car_form = CarModelForm()
    return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )

class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', { 'new_car_form': new_car_form })

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():  # Verifica se os formularios são validos
            new_car_form.save()  # Salva os dados
            return redirect('cars_list')  # Retorna para a pagina de lista de carros
        return render(request, 'new_car.html', { 'new_car_form': new_car_form })
