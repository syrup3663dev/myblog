from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='index'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('create/', views.ArticleCreateView.as_view(), name='create'),
]
