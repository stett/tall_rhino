from django import template
from blog.models import *

register = template.Library()


@register.inclusion_tag("comments.html")
def comments(subject):
    comments = subject.comments.filter(published=True)
    if type(subject) is Post:
        comments = comments.filter(parent=None)
    return {"comments": comments}
