from django.urls import path
from .views import ProfileView
urlpatterns = [
    path('/home/<int:id>', ProfileView.as_view(), name='home')
]