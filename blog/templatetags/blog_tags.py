from django import template
from blog.models import Post,Comment
from blog.models import category
register = template.Library()
@register.simple_tag(name='totalposts')
def function():
    posts=Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()
    

@register.simple_tag(name='posts')
def function():
    posts=Post.objects.filter(status=1)
    return posts
@register.filter
def snippet(value):
    return value[:100]
@register.inclusion_tag('blog/blog-popular-post.html')
def latestposts(arg=2):
    posts=Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}
@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categories=category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}
