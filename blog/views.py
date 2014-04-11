from .models import *

# CBVs

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
class BlogView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'posts'
    paginate_by = 3


# APIs

#from rest_framework.generics import ListAPIView
#from .serializers import *
#class PostsAPIView(ListAPIView):
#    model = Post
#    serializer_class = PostSerializer
#    def get_queryset(self):
#        queryset = self.model.objects.all()
#        if 'newest' in self.kwargs:
#            queryset = queryset.filter(date__le=self.kwargs['newest'])
#        if 'oldest' in self.kwargs:
#            queryset = queryset.filter(date__ge=self.kwargs['oldest'])
#        return queryset


