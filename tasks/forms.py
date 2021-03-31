# Django
from django import forms

# Models
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ('name', 'description', 'completed')

    def __init__(self, *args, **kwargs):
        self.list = kwargs.pop('list')
        super(TaskForm, self).__init__(*args, **kwargs)

    def save(self):
        self.instance.list = self.list

        return super().save()
