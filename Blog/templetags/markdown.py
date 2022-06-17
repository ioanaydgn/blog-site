import markdown

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_md(field):
    return mark_safe(markdown.markdown(field))
