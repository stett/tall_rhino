from django import template

register = template.Library()


@register.inclusion_tag("imageset.html")
def imageset(images):
    return {"images": images}
