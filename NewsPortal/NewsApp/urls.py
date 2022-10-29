from django.urls import path
from .views import PostsList, PostDetail, NewsCreate, ArticleCreate

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
]