"""Lists URLs."""

# Django
from django.urls import path

# View
from lists import views


urlpatterns = [
    path(
        route='',
        view=views.IndexView.as_view(),
        name='index'
    ),

    path(
        route='lists/new',
        view=views.CreateListView.as_view(),
        name='new'
    )
]
