# Django
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView

# Models
from lists.models import List
from tasks.models import Task

# Form
from tasks.forms import TaskForm


class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/form.html'
    form_class = TaskForm

    def get_success_url(self):
        pk = self.object.list.pk
        return reverse('lists:show', kwargs={'pk': pk})

    def get_form_kwargs(self):
        kwargs = super(CreateTaskView, self).get_form_kwargs()
        list = List.objects.get(pk=self.kwargs['pk'])
        kwargs.update({'list': list})

        return kwargs


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/form.html'
    model = Task
    fields = ['name', 'description']

    def get_success_url(self):
        pk = self.object.list.pk
        return reverse('lists:show', kwargs={'pk': pk})
