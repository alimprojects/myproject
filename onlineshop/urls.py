from django.urls import path
from .views import *

urlpatterns = [
    path('homepage/', landing, name='index'),
    path('<int:id>', product, name = 'product'),
    path('contact/', contact, name = 'contact'),
    path('review/',  create_review,  name = 'review'),
]