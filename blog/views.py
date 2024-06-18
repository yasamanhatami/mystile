from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def blog_view(request):
    posts=Post.objects.filter(published_date__lte=timezone.now(),status=1)
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)
def blog_single(request,pid):
    post=get_object_or_404(Post,id=pid,status=1,published_date__lte=timezone.now())
    post.counted_views=post.counted_views+1
    post.save()
    paginator = Paginator(post,10)
    page = request.GET.get('page')
    try:
        object= paginator.page(page)
    except PageNotAnInteger:
        object= paginator.page(1)
    except EmptyPage:
        object= paginator.page(paginator.num_pages)
    context={'post':post,'object':object}
    return render(request,'blog/blog-single.html',context)
#def test(request,pid):
    #posts=get_object_or_404(Post,id=pid)
    #context={'posts':posts}
    #return render(request,'test.html',context)