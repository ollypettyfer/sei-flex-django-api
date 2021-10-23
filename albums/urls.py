from django.urls import path
from .views import index, AlbumsListView
from .views import AlbumDetailView

urlpatterns = [
    path("", index),
    path("api/", AlbumsListView.as_view()),
    path("api/<int:id>/", AlbumDetailView.as_view()),
]
