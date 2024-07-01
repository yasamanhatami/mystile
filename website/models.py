from django.db import models

# Create your models here.
class Cantact(models.Model):
    name=models.CharField(max_length=225)
    email=models.EmailField()
    subject=models.CharField(null=True,blank=True,max_length=225)
    message=models.TextField()
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    class Meta():
        ordering = ('created_date',)
    def __str__(self):
        return '{} {}'.format(self.name, self.id)
class Newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email
