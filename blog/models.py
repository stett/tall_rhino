from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255)
    date = models.DateTimeField()
    published = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date', ]
    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey('Post', related_name='images')
    image = models.ImageField(upload_to='blog')
    description = models.TextField(blank=True, null=True)
    order = models.IntegerField()

class PostComment(models.Model):
    post = models.ForeignKey('Post', related_name='comments')
    parent = models.ForeignKey('PostComment', related_name='comments', blank=True, null=True)
    user = models.CharField(max_length=255, default='anonymous')
    content = models.TextField()
    date = models.DateTimeField()
    published = models.BooleanField(default=False)
    class Meta:
        ordering = ['-post__date', '-date', ]
    def __str__(self):
        return '%s: %s' % (self.user, self.content)
