from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from .models import *

# FBVs

from django.shortcuts import render


def archive_view(request):
    posts = {}
    for post in Post.objects.published():
        if post.date.year not in posts:
            posts[post.date.year] = [post, ]
        else:
            posts[post.date.year].append(post)
    context = {"posts": posts}
    return render(request, "archive.html", context)

# CBVs

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"

    def get_object(self):
        object = super(PostDetailView, self).get_object()
        if not object.published:
            raise Http404
        return object


class PostListView(ListView):
    model = Post
    context_object_name = "posts"

    def get_queryset(self):
        if (self.request.GET.get('draft') is not None and
            self.request.user.is_authenticated() and
            self.request.user.is_superuser):
            return Post.objects.all()
        else:
            return Post.objects.published()

# API Views

from rest_framework.views import APIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView)


class ReadUpdateDeletePostAPIView(RetrieveUpdateDestroyAPIView):
    model = Post


class ListCreatePostAPIView(ListCreateAPIView):
    model = Post


class PublishPostAPIView(APIView):

    def post(self, request, pk):
        if (not self.request.user.is_authenticated and
                self.request.user.is_superuser):
            raise PermissionDenied

        post = get_object_or_404(Post, pk=pk)
        post.published = True
        post.save()

        return redirect('post', pk=post.pk)
