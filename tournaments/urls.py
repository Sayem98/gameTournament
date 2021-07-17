from django.urls import path, include
from .views import TournamentsView
urlpatterns = [
    path('new', TournamentsView.as_view(), name='new_tournaments')
]