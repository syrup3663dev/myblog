from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),  # 一覧表示
    path('create/', views.ArticleCreateView.as_view(), name='create'),  # 新規投稿
    path('<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='update'),  # 記事編集
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='delete'),  # 記事削除
]
