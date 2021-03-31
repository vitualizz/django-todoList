# Django
from django import forms

# Models
from lists.models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ListForm, self).__init__(*args, **kwargs)

    def save(self):
        self.instance.user = self.user

        return super().save()
