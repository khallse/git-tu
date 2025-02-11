
from django import template
from ..models import *
register = template.Library()


@register.simple_tag
def title():
    return "وبلاگ جنگویی"

@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return{
        "category":Category.objects.filter(status=True)
    }