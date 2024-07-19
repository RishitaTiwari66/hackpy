# news/urls.py

from django.urls import path
from .views import NewsListView, NewsDetailView, NewsCreateView, vote_news

urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/new/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/vote/<str:vote_type>/', vote_news, name='vote_news'),
]
