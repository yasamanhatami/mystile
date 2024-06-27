from django import template
from blog.models import Post
from django.utils import timezone
register = template.Library()
@register.inclusion_tag('website/website-latest-post.html')
def blogposts(arg=6):
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)[:arg]
    return {'posts':posts}
