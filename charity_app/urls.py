from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about-us/', about, name='about'),
    path('contact-us/', contact, name='contact'),
    path('about-the-founder/', mainfounder, name='mainfounder'),
    path('event-details/<slug>/', eventdetails, name='eventdetails'),
    path('event-registration/<slug>/', eventregistration, name='eventregistration'),
    path('donate-section/<slug>/', donatesection, name='donatesection'),
    path('at-a-glance/', glance, name='glance'),
    path('partners-and-networks/', partnersnetworks, name='partnersnetworks'),
    path('awards-recognation/', awardsrecognation, name='awardsrecognation'),
    path('donate/', donate, name='donate'),
    path('blog-list/', bloglist, name='bloglist'),
    path('blog-details/<pk>/', blogdetails, name='blogdetails'),
    path('gallery-list/', gallerylist, name='gallerylist'),
    path('social-development/', socialdevelopment, name='socialdevelopment'),
    path('become-a-volunteer/', becomeavolunteer, name='becomeavolunteer'),
    path('send-gift/', sendgift, name='sendgift'),
    path('founder/<pk>/', founder, name='founder'),
    path('about/', aboutmore, name='aboutmore'),
    path('notice/', notice, name='notice'),
]