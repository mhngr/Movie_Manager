from django.urls import path
from .views import CreateMovie, MovieDetail, MovieList, CreateArtist, ArtistsList, ArtistDetail, InstalledExtensions
from .views import FilterArtists, ManageActors, ManageDirectors, APICallData

urlpatterns = [
    path("create_movie/", CreateMovie.as_view()),
    path("movie_list/", MovieList.as_view()),
    path("movie_detail/", MovieDetail.as_view()),
    path("create_artist/", CreateArtist.as_view()),
    path("artists_list/", ArtistsList.as_view()),
    path("artist_detail/", ArtistDetail.as_view()),
    path("installed_extensions/", InstalledExtensions.as_view()),
    path("filter_artists/", FilterArtists.as_view()),
    path("manage_actors/", ManageActors.as_view()),
    path("manage-directors/", ManageDirectors.as_view()),
    path("API_call_data/", APICallData.as_view()),

]