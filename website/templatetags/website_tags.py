from django import template
from blog.models import Post
from django.utils import timezone
register = template.Library()
@register.simple_tag(name='blogposts')
def function():
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    return posts
