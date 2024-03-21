from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def register_view(request):
    if request.method == "POST": # Verifica se o método recebido é o POST
        user_form = UserCreationForm(request.POST) # Cria o formulário com os dados preenchidos
        if user_form.is_valid(): # Verifica se os campos são validos
            user_form.save() # Salva os dados
            return redirect('login') # Redireciona o usuario para a tela de login
    else:
        user_form = UserCreationForm() # Cria o formulário para preencher os dados
    return render(request, 'register.html', {'user_form': user_form}) # Renderiza a pagina HTML

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) # Para validar o login

        if user is not None:
            login(request, user) # Realiza o login
            return redirect('cars_list') # Redireciona o usuario para a tela de carros
        else:
            login_form = AuthenticationForm() # Caso a autenticação falhe, recria o formulario novamente
    else:
        login_form = AuthenticationForm() # Caso a autenticação esteja vazia, recria o formulario novamente
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('cars_list')