# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

# Model
from lists.models import List

# Form
from lists.forms import ListForm


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'lists/index.html'
    model = List
    paginate_by = 20
    context_object_name = 'lists'


class CreateListView(LoginRequiredMixin, CreateView):
    template_name = 'lists/new.html'
    form_class = ListForm
    success_url = reverse_lazy('lists:index')

    def get_form_kwargs(self):
        kwargs = super(CreateListView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
