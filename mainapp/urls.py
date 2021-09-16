from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('loyihalar/',views.loyihalar, name='loyihalar'),
    path('videolar/',views.videolar, name='videolar'),
    path('rasmlar/',views.rasmlar, name='rasmlar'),
    path('contact/',views.contact, name='contact')
]