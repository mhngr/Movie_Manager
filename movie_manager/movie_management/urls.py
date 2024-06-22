from django.urls import path
from .views import CreateMovie,  MovieList, CreateArtist, ArtistsList,  InstalledExtensions, APICallData, DeleteMovie

urlpatterns = [
    path("create_movie/", CreateMovie.as_view()),
    path("movie_list/", MovieList.as_view()),
    path("create_artist/", CreateArtist.as_view()),
    path("artists_list/", ArtistsList.as_view()),
    path("installed_extensions/", InstalledExtensions.as_view()),
    path("API_call_data/", APICallData.as_view()),
    path("<int:id>/delete_movie/", DeleteMovie.as_view()),

]