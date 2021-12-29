from django.urls import path
from basic_api.views import article_list, article_detail


urlpatterns = [
    path('article/', view=article_list),
    path('detail/<int:pk>', view=article_detail),
]
