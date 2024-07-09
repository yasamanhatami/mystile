from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=225)
    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    image=models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=225)
    content=models.TextField()
    tags = TaggableManager()
    category=models.ManyToManyField(category)
    counted_views= models.IntegerField(default=0)
    status=models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)#2024-03-30 11:10:56.530638

    class Meta:
        ordering=['-published_date']
    def __str__(self):
        return '{}-{}'.format(self.title, self.id)
    #def snippets(self):
        #return self.content[100] +'...' 

    def get_absolute_url(self):
        return reverse('blog:single',kwargs={'pid':self.id})

