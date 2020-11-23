from django.forms import ModelForm
from .models import task

class TaskForm(ModelForm):
    class Meta:
        model = task
        fields = ('title', 'description')
    """ title = forms.CharField(label = "Название задачи", max_length = 150)
    description = forms.CharField(label = "Описание задачи", max_length = 250, widget=forms.Textarea(attrs={"rows":5, "cols":20})) """