# Django
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView

# Model
from lists.models import List
from tasks.models import Task

# Form
from lists.forms import ListForm


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'lists/index.html'
    model = List
    paginate_by = 20
    context_object_name = 'lists'


class ShowListView(LoginRequiredMixin, DetailView):
    model = List
    template_name = 'lists/show.html'
    context_object_name = 'list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list = self.get_object()
        context['tasks'] = Task.objects.filter(list=list).order_by('-created')
        return context


class CreateListView(LoginRequiredMixin, CreateView):
    template_name = 'lists/form.html'
    form_class = ListForm
    success_url = reverse_lazy('lists:index')

    def get_form_kwargs(self):
        kwargs = super(CreateListView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UpdateListView(LoginRequiredMixin, UpdateView):
    template_name = 'lists/form.html'
    model = List
    fields = ['name', 'description']

    def get_success_url(self):
        pk = self.object.pk
        return reverse('lists:show', kwargs={'pk': pk})
