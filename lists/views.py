# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Model
from lists.models import List


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'lists/index.html'
    model = List
    paginate_by = 20
    context_object_name = 'lists'
