from django.urls import path
from basic_api import views


urlpatterns = [
    #path('article/', view=article_list),
    path('articles/', view=views.ArticleListAPIView.as_view()),
    #path('detail/<int:pk>', view=article_detail),
    path('articles/<int:pk>', view=views.ArticleDetailAPIView.as_view()),
]
