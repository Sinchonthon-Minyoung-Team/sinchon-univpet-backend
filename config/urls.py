from django.contrib import admin
from django.urls import include, path
from posts.views import PostViewSet
from posts.views import SortedPostListView  # 해당 뷰를 import 해야합니다.

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

from accounts.views import AccountCreateRetrieveViewSet
from auths.views import OAuthTokenObtainView

accounts_router = DefaultRouter()
accounts_router.register(r'accounts', AccountCreateRetrieveViewSet, basename='accounts')

posts_router = DefaultRouter()
posts_router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/<str:provider>/token', OAuthTokenObtainView.as_view(), name='token_obtain'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(accounts_router.urls)),
    path('sorted_posts/', SortedPostListView.as_view(), name='sorted-posts'),  # d-day로 정렬된 리스트 불러옴
    path('', include(posts_router.urls)),
]
