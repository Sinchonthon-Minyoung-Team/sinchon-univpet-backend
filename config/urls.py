from django.contrib import admin
from django.urls import include, path
from accounts.views import AccountCreateRetrieveViewSet
from posts.views import PostViewSet, sorted_post_list
# from posts.views import SortedPostListView  # 해당 뷰를 import 해야합니다.

from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter
from auths.views import OAuthTokenObtainView
from accounts.views import AccountCreateRetrieveViewSet

from posts.views import PostViewSet, CommentViewSet

posts_router = DefaultRouter()
posts_router.register(r'posts', PostViewSet, basename='posts')

comments_router = DefaultRouter()
comments_router.register(r'comments', CommentViewSet, basename='comments')


accounts_router = DefaultRouter()
accounts_router.register(r'accounts', AccountCreateRetrieveViewSet, basename='accounts')

posts_router = DefaultRouter()
posts_router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/<str:provider>/token',
        OAuthTokenObtainView.as_view(), name='token_obtain'),
    path('auth/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(posts_router.urls)),
    path('', include(accounts_router.urls)),
    path('sorted_posts/', sorted_post_list, name='sorted-posts'),
    path('', include(posts_router.urls)),
    path('likes/', include('likes.urls')),
]
