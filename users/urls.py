from django.urls import path
from .views import profile as profile_view
from .views import delete_user as delete_view
from .views import signup as signup_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('profile/', profile_view, name='profile'),
    path('delete/', delete_view, name='delete'),
]