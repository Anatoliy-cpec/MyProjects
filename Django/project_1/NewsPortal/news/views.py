from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.db.models import Exists, OuterRef
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
)
from .filters import PostSearchFilter
from .forms import PostForm, PostArticleForm, PostNewsForm
from .models import *


class PostSearch(ListView):
    model = Post
    ordering = '-creation_date'
    template_name = 'post_search.html'
    context_object_name = 'search'
    paginate_by = 8

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostSearchFilter(self.request.GET, queryset)
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context

class PostsList(ListView):
    model = Post
    ordering = '-creation_date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostSearchFilter(self.request.GET, queryset)
       return self.filterset.qs

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       # Добавляем в контекст объект фильтрации.
       context['filterset'] = self.filterset
       return context
    
    

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'




class PostArticleCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostArticleForm
    model = Post
    template_name = 'post_article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choise = 'AR'
        return super().form_valid(form)
    
class PostArticleUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostArticleForm
    model = Post
    template_name = 'post_article_edit.html'

class PostArticleDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'post_article_delete.html'
    success_url = reverse_lazy('posts')



    
class PostNewsCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostNewsForm
    model = Post
    template_name = 'post_news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.choise = 'NE'
        return super().form_valid(form)

class PostNewsUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostNewsForm
    model = Post
    template_name = 'post_news_edit.html'

class PostNewsDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'post_news_delete.html'
    success_url = reverse_lazy('posts')





class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

class PostDelete(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')