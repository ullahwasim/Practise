"""todowoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('currenttodo/', views.currenttodo, name="currenttodo"),
    path('createtodo/', views.createtodo, name="createtodo"),
    path('login/', views.userlogin, name="userlogin"),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_id>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_id>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_id>/delete', views.deletetodo, name='deletetodo'),
    path('methodview/', views.MethodView.as_view()),
    path('templateview/', views.Template.as_view()),
    path('templateviewinjection/', views.TemplateViewInjection.as_view()),
    path('todo_list_view/', views.TodoListView.as_view()),
    path('todo_detail_view/<int:pk>/', views.TodoDetailView.as_view()),
    path('todo_create_view/', views.TodoCreateView.as_view())
]
