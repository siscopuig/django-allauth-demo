from django.urls import path
from .views import profile as profile_view

urlpatterns = [
    path('profile/', profile_view, name='profile')
]