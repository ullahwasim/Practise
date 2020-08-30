from django.shortcuts import render
import random


# from django.http import HttpResponse


# Create your views here.

def home(request):
    # return HttpResponse('asd')
    return render(request, 'passwordgenerator/index.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specail'):
        characters.extend(list('!@#$%^&('))

    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'passwordgenerator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'passwordgenerator/about.html')
