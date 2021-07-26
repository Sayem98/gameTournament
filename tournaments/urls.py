from django.urls import path, include
from .views import TournamentsView, All_TournamentsView, A_tournamentView, RegisterTournamentView, UpdateTournamentView
urlpatterns = [
    path('new', TournamentsView.as_view(), name='new_tournaments'),
    path('all', All_TournamentsView.as_view(), name='all_tournaments'),
    path('a_tournament/<int:id>', A_tournamentView.as_view(), name='a-tournament'),
    path('register-tournament/<int:id>', RegisterTournamentView.as_view(), name='register-a-tournament'),
    path('update/<int:id>', UpdateTournamentView.as_view(), name='update-tournament')
]