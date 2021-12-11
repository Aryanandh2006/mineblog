from django.shortcuts import render, get_object_or_404
from django.template import context
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import post
from .forms import PostForm
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model = post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetail(DetailView):
    model = post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    #fields = '__all__'


class UpdatePostView(UpdateView):
    model = post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
    #fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
