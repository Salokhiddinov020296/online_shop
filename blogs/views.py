from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from blogs.models import PostModel


class PostListView(ListView):
    queryset = PostModel.objects.order_by('-id')
    template_name = 'blog.html'


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'blog-details.html'

