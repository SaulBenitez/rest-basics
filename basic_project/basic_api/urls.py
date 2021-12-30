from django.urls import path
from basic_api import views


urlpatterns = [
    path('articles/', view=views.ArticleListAPIView.as_view()),
    path('articles/<int:pk>/', view=views.ArticleDetailAPIView.as_view()),
    path('generic/articles/<int:id>/', view=views.GenericAPIView.as_view()),
]
