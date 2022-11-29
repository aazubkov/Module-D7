# from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .form import PostForm
from .models import Post
from .filters import PostFilter


# Create your views here.
class NewsList(ListView):
    model = Post
    ordering = '-posted'
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    paginate_by = 4


class NewsId(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'news_id'


class PostSearch(ListView):
    model = Post
    ordering = '-posted'
    template_name = 'search.html'
    context_object_name = 'news_list'
    # paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class NewsCreate(PostCreate):
    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'N'
        return super().form_valid(form)


class ArticlesCreate(PostCreate):
    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'A'
        return super().form_valid(form)


class PostEdit(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
