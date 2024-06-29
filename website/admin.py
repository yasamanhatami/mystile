from django.contrib import admin
from website.models import Cantact,Newsletter
# Register your models here.

class CantactAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=('name','email','created_date')
    list_filter=('email',)
    search_fields=('name','message')
admin.site.register(Cantact,CantactAdmin)
admin.site.register(Newsletter)