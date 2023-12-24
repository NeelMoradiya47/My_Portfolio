from django.urls import path
from . import views

app_name = 'portfolioapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_me', views.about_me, name='about_me'),
    path('projects', views.projects, name='projects'),
    path('contact_me', views.contact_me, name='contact_me'),
    path('insert_data', views.insert_data, name='insert_data'),
]
