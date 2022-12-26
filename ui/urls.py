from django.urls import path
from . import views
from chirps import views as chirp_views

urlpatterns = [
    path("", views.home, name="ui-home"),
    path('<str:username>/chirp/<str:id>', chirp_views.view_chirp, name='view-chirp'),
    path('<str:username>/chirp/<str:id>/edit', chirp_views.edit_chirp, name='edit-chirp'),
    path('<str:username>/chirp/<str:id>/upvote', chirp_views.upvote, name='up-vote'),
    path('<str:username>/chirp/<str:id>/downvote', chirp_views.downvote, name='down-vote'),
]
