# posts/urls.py

from django.urls import path
from . import views
from .views import get_petition_detail 

urlpatterns = [
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('petitions/<int:post_id>/', get_petition_detail, name='petition-detail'),

]
