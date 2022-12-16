from django.urls import path
from . import views
from chirps import views as chirp_views

urlpatterns = [
    path("", views.home, name="ui-home"),
    path('<str:username>/chirp/<str:id>', chirp_views.view_chirp, name='view-chirp'),
    path('<str:username>/chirp/<str:id>/edit', chirp_views.edit_chirp, name='edit-chirp'),
]
