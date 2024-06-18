from django.urls import path
from .views import RegisterMovie

urlpatterns = [
    path("register_movie/", RegisterMovie.as_view())
]