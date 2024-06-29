from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from website.forms import ContactForm,NewsletterForm
# Create your views here.
def index_views (request):
    return render(request,'website/index.html')
def about_views (request):
    return render(request,'website/about.html')
def contact_views (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form=ContactForm()
    return render(request,'website/contact.html',{'form':form})
def newsletter_views(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
        
        

def test_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form=ContactForm()
    return render(request,'test.html',{'form':form})


