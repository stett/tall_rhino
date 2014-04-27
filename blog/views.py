from .models import *

# CBVs

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
class BlogView(ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = "posts"
    paginate_by = 3
class PostView(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"
class CommentsView(DetailView):
    model = Post
    template_name = "comments_base.html"
    context_object_name = "post"
class EditBlogView(ListView):
    model = Post
    template_name = "edit-blog.html"
    context_object_name = "posts"
class EditPostView(DetailView):
    model = Post
    template_name = "edit-post.html"
    context_object_name = "post"


# API Views

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
class ReadUpdateDeletePostAPIView(RetrieveUpdateDestroyAPIView):
    model = Post
class ListCreatePostAPIView(ListCreateAPIView):
    model = Post
