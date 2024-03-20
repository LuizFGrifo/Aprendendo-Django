from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def register_view(request):
    if request.method == "POST": # Verifica se o método recebido é o POST
        user_form = UserCreationForm(request.POST) # Cria o formulário com os dados preenchidos
        if user_form.is_valid(): # Verifica se os campos são validos
            user_form.save() # Salva os dados
            return redirect('cars_list') # Redireciona o usuario para a tela de login
    else:
        user_form = UserCreationForm() # Cria o formulário para preencher os dados
    return render(request, 'register.html', {'user_form': user_form}) # Renderiza a pagina HTML