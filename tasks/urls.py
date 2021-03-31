"""Tasks URLs."""

# Django
from django.urls import path

# View
from tasks import views

urlpatterns = [
    path(
        route='lists/<slug:pk>/tasks/new',
        view=views.CreateTaskView.as_view(),
        name='new'
    ),

    path(
        route='tasks/<slug:pk>/edit',
        view=views.UpdateTaskView.as_view(),
        name='new'
    ),
]
