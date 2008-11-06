"""
Fragment rendering template tags.
"""

from django import template
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe
from django.core.exceptions import ObjectDoesNotExist

from fraggle.models import Fragment

register = template.Library()

@register.simple_tag
def render_fragment(fragment_id):
    """
    Render an html fragment.

    Usage::
        {% load render_fragment %}
        {% render_fragment [id] %}

    """
    try:
        int(fragment_id)
    except ValueError:
        return ''
    try: 
        fragment = Fragment.objects.get(pk=fragment_id)
        return mark_safe(force_unicode(smart_str(fragment.html)))
    except ObjectDoesNotExist:
        return ''
