from django.shortcuts import redirect, render
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo e-mail não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não podem ser diferentes')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('e-mail já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=nome,email=email,password=senha)
        user.save()
        print('Usuário cadastrado com sucesso!!!')
        return redirect('login')
    else:
        return render(request,'usuarios/cadastro.html')

def login(request):
    return render(request,'usuarios/login.html')

def logout(request):

    return

def dashboard(request):

    return
