from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    # pass
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']
