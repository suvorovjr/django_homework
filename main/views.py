from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(f'Пользователя зовут {name}. Его емэйл {email} и пароль {password}.')
    return render(request, 'main/contacts.html')
