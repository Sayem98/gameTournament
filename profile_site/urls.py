from django.urls import path
from .views import ProfileView, HomeView, UpdateAccountView

urlpatterns = [
    path('home', HomeView.as_view(), name='Go-to-home'),
    path('home/<int:id>', ProfileView.as_view(), name='home'),
    path('home/account', UpdateAccountView.as_view(), name='my-account')
]

