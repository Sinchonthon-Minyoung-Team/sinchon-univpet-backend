"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, include, path

from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework.routers import DefaultRouter

from accounts.views import AccountCreateRetrieveViewSet
from auths.views import OAuthTokenObtainView

accounts_router = DefaultRouter()
accounts_router.register(r'accounts', AccountCreateRetrieveViewSet, basename='accounts')

from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet

posts_router = DefaultRouter()
posts_router.register(r'posts', PostViewSet, basename='posts')

accounts_router = DefaultRouter()
accounts_router.register(r'accounts', AccountCreateRetrieveViewSet, basename='accounts')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/<str:provider>/token',
         OAuthTokenObtainView.as_view(), name='token_obtain'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(accounts_router.urls)),

    path('', include(posts_router.urls)),
]
