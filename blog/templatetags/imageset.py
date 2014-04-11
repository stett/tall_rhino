from django import template
#from blog.models import *

register = template.Library()

class ImageSetNode(template.Node):
    def __init__(self, post):
        self.post = post
    def render(self, context):
        t = template.loader.get_template("imageset.html")
        return t.render(template.Context({"post": self.post}, autoescape=context.autoescape))

@register.tag(name="imageset")
def imageset(parser, token):
    tag_name, post = token.split_contents()
    return ImageSetNode(post)
