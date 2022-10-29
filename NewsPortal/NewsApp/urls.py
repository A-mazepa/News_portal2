from django.urls import path
from .views import PostsList, PostDetail, NewsCreate, ArticleCreate, ArticleUpdate, NewsUpdate, ArticleDelete, NewsDelete

urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='articles_update'),
    path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='articles_delete'),

]