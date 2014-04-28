from django.views.generic import TemplateView
from blog.views import PostDetailView, PostListView
class BlogView(PostListView):
    template_name = "blog.html"
    paginate_by = 3
class PostView(PostDetailView):
    template_name = "post.html"
class CommentsView(PostDetailView):
    template_name = "comments_base.html"
class EditBlogView(PostListView):
    template_name = "edit-blog.html"
class EditPostView(PostDetailView):
    template_name = "edit-post.html"
class AboutView(TemplateView):
    template_name = "about.html"

# Legacy Views
from blog.models import Post
from django.shortcuts import redirect, get_object_or_404
def legacy_post_redirect(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return redirect(post)
