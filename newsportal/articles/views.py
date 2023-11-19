from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Article
from django.urls import reverse_lazy
from django.core.paginator import Paginator


class ArticlesListView(ListView):
    model = Article
    template_name = 'articles/articles_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 10  # Количество элементов на странице

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(context['object_list'], self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['articles'] = page_obj
        return context


class ArticlesCreateView(CreateView):
    model = Article
    fields = ['title', 'content']
    success_url = reverse_lazy('articles_list')
    template_name = 'articles/articles_create.html'


class ArticlesUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'articles/articles_update.html'
    success_url = reverse_lazy('articles_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class ArticlesDeleteView(DeleteView):
    model = Article
    template_name = 'articles/articles_delete.html'
    success_url = reverse_lazy('articles_list')
