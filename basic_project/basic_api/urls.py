from django.urls import path, include
from basic_api import views
from rest_framework.routers import DefaultRouter

#from basic_api.views import ArticleViewSet
#from basic_api.views import ArticleGenericViewSet

router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('genarticles', views.ArticleGenericViewSet, basename='genarticles')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('articles/', view=views.ArticleListAPIView.as_view()),
    path('articles/<int:pk>/', view=views.ArticleDetailAPIView.as_view()),
    path('generic/articles/<int:id>/', view=views.GenericAPIView.as_view()),
]
