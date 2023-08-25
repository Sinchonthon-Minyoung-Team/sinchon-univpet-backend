from django.urls import path
from . import views
from .views import UserProfileView


urlpatterns = [
    path('<int:user_id>/', UserProfileView.as_view(), name='user-profile'),
]