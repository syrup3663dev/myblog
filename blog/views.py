from django.shortcuts import render
from django.views import generic
from .models import Article
from .forms import ArticleCreateForm, ArticleUpdateForm
from django.urls import reverse_lazy

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
    form_class = ArticleCreateForm
    success_url = '/'  # 成功時にリダイレクトするURL

class ArticleUpdateView(generic.UpdateView):
    model = Article
    template_name = 'update.html'
    form_class = ArticleUpdateForm
    success_url = '/'

class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = 'delete.html'
    success_url = reverse_lazy('index')