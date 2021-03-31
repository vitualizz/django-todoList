# Django
from django import forms

# Models
from lists.models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('user', 'name', 'description')
