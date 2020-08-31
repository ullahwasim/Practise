from django.utils import timezone

from django.contrib.auth import login, authenticate, logout
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView

from todo.models import Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Create your views here.
from django.views.decorators.http import require_http_methods


def home(request):
    if request.user.is_authenticated:
        return redirect('currenttodo')
    else:
        return redirect('usersignup')


@require_http_methods(["GET", "POST"])
def usersignup(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'todo/signup.html', {'form': UserCreationForm()})
        elif request.method == 'POST':
            try:
                if request.POST.get('password1') != request.POST.get('password2') or (
                        request.POST['username'] == '' or request.POST['password1'] == ''):
                    return render(request, 'todo/signup.html', {'form': UserCreationForm(), 'error': 'Username OR '
                                                                                                     'Password is not '
                                                                                                     'same!'})
                else:
                    user = User.objects.create_user(username=request.POST.get('username'),
                                                    password=request.POST.get('password1'))
                    user.save()
                    login(request, user)
                    return redirect('home')
            except IntegrityError:
                return render(request, 'todo/signup.html', {'form': UserCreationForm(),
                                                            'error': 'That username has already been taken. Please '
                                                                     'choose '
                                                                     'a new username'})
            except:
                return render(request, 'todo/signup.html',
                              {'form': UserCreationForm(), 'error': 'Something went wrong!'})
    else:
        return redirect('home')


@login_required
def currenttodo(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True).order_by("-created")
    return render(request, 'todo/currenttodo.html', {'todos': todos})


def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todo/completedtodo.html', {'todos': todos})


@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    elif request.method == 'POST':
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'todo/createtodo.html',
                          {'form': TodoForm(), 'error': 'Bad data passed in. Try again.'})
        except:
            return render(request, 'todo/createtodo.html',
                          {'form': TodoForm(), 'error': 'Something went wrong. Please try later!'})


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('currenttodo')
        # return HttpResponse('None')
    if request.method == 'GET':
        return render(request, 'todo/userlogin.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            return render(request, 'todo/userlogin.html', {'form': AuthenticationForm(), 'error': 'Username and '
                                                                                                  'password did not '
                                                                                                  'match'})
        else:
            login(request, user)
            return redirect('currenttodo')


@login_required
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home')


@login_required
def completetodo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodo')
    else:
        return redirect('home')


@login_required
def deletetodo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodo')


@login_required
def viewtodo(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodo')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error': 'Bad info'})


class MethodView(View):
    def get(self, request):
        return HttpResponse('Method View')


class Template(TemplateView):
    template_name = 'todo/templateview.html'


class TemplateViewInjection(TemplateView):
    template_name = 'todo/templateviewinjection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Class Based View Injection"
        return context


class TodoListView(ListView):
    model = User


class TodoDetailView(DetailView):
    model = User


class TodoCreateView(CreateView):
    template_name = 'todo/todo_form.html'
    model = User
    fields = ('username', 'password')
