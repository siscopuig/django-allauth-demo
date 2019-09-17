from django.urls import path
from .views import profile as profile_view
from .views import delete_user as delete_view
# from .views import disconnect as disconnect_view


urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('delete/', delete_view, name='delete'),
    # path('disconnect/', disconnect_view, name='disconnect')
]