from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    post=get_object_or_404(Post,id=pid,status=1,published_date__lte=timezone.now())
    post.counted_views=post.counted_views+1
    post.save()
    next_post = Post.objects.filter(id__gt=pid,published_date__lte=timezone.now(),status=1).first()
    previous_post = Post.objects.filter(id__lt=pid,published_date__lte=timezone.now(),status=1).last()
    context={'post':post,'next_post':next_post,'previous_post':previous_post}
    return render(request,'blog/blog-single.html',context)
def test(request):
    #posts=get_object_or_404(Post,id=pid)
    #context={'posts':posts}
    return render(request,'test.html')