from django.urls import path
from website.views import *
urlpatterns = [
    path('home',index_views),
    path('about',about_views),
    path('contact',contact_views)

]