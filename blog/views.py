from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def blog_view(request,**kwargs):
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1).order_by('published_date')
    if kwargs.get('cat_name')!=None:
        posts=Post.objects.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts=Post.objects.filter(author__username=kwargs['author_username'])
    
    posts=Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts=posts.get_page(page_number)
    except PageNotAnInteger:
        posts=posts.get_page(1)
    except EmptyPage:
        posts=posts.get_page(1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    post=get_object_or_404(Post,id=pid,status=1,published_date__lte=timezone.now())
    post.counted_views=post.counted_views+1
    post.save()
    next_post = Post.objects.filter(id__gt=pid,published_date__lte=timezone.now(),status=1).last()
    previous_post = Post.objects.filter(id__lt=pid,published_date__lte=timezone.now(),status=1).first()
    context={'post':post,'next_post':next_post,'previous_post':previous_post}
    return render(request,'blog/blog-single.html',context)
#def test(request):
    #posts=get_object_or_404(Post,id=pid)
    #context={'posts':posts}
    #return render(request,'test.html')
def blog_search(request):
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    if request.method == "GET":
        if s:=request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)