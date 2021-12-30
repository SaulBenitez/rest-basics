from django.urls import path, include
from basic_api import views
from rest_framework.routers import DefaultRouter

from basic_api.views import ArticleViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('articles/', view=views.ArticleListAPIView.as_view()),
    path('articles/<int:pk>/', view=views.ArticleDetailAPIView.as_view()),
    path('generic/articles/<int:id>/', view=views.GenericAPIView.as_view()),
]
