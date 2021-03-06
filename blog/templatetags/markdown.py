from django import template
from django.utils.safestring import mark_safe
from django.utils.encoding import force_unicode
from django.template.defaultfilters import stringfilter
import markdown2

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def markdown(value):
    return mark_safe(markdown2.markdown(force_unicode(value), safe_mode=True))
