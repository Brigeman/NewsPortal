from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    ordering = ['-created_at']


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'article'


class NewsCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'category']
    template_name = 'news/news_create.html'
    success_url = reverse_lazy('news_list')


class NewsUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'category']
    success_url = reverse_lazy('news_list')
    template_name = 'news/news_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class NewsDeleteView(DeleteView):
    model = Post
    template_name = 'news/news_delete.html'
    success_url = reverse_lazy('news_list')
