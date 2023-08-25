# likes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/toggle/', views.LikeToggle.as_view(), name='like-toggle'),
    path('<int:post_id>/count/', views.LikeCountView.as_view(), name='like-count'),
]
