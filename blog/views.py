from django.shortcuts import render
from django.views import generic
from .models import Article
from .forms import ArticleForm

class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 5
    template_name = 'index.html'

    def get_context_data(self):
        context = super().get_context_data()
        return context

class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'detail.html'

class ArticleCreateView(generic.CreateView):
    model = Article
    template_name = 'create.html'
    form_class = ArticleForm
    success_url = '/'  # 成功時にリダイレクトするURL