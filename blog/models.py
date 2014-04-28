from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

class PostManager(models.Manager):
    def published(self):
        return Post.objects.filter(published=True)
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    date = models.DateTimeField()
    published = models.BooleanField(default=False)
    objects = PostManager()
    class Meta:
        ordering = ['-date', ]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post', args=[self.id])

class PostImage(models.Model):
    post = models.ForeignKey('Post', related_name='images')
    image = models.ImageField(upload_to='blog')
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField()
    archive = models.BooleanField(default=True)
