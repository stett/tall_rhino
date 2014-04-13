from django import template

register = template.Library()

class ImageSetNode(template.Node):
    def __init__(self, images):
        self.images = images
    def render(self, context):
        t = template.loader.get_template("imageset.html")
        return t.render(template.Context({"images": self.images}, autoescape=context.autoescape))

@register.simple_tag
def imageset(images):
    return ImageSetNode(images)
