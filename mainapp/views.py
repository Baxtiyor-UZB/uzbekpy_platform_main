from typing import ContextManager
from django.contrib import admin
from django.shortcuts import render, redirect
from . models import Home, Hometext, About, AboutText, Mavzu, Images, Video
from django.utils import timezone
from mainapp.forms import MyCommentForm
from django.contrib import messages

# Create your views here.

def index(request):
    post = Home.objects.all()
    post2 = Hometext.objects.all()
    context = {
        'post' : post,
        'post2' : post2
    }
    return render(request, 'index.html', context)

def about(request):
    abouts = About.objects.all()
    abouttext = AboutText.objects.all()
    context = {
        'abouts' : abouts,
        'abouttext' : abouttext
    }
    return render(request, 'haqimizda.html', context)    

def videolar(request):
    
    video = Video.objects.all()
    context = {
        'video' : video
    }
    return render(request, 'videolar.html', context) 
def rasmlar(request):
    images = Images.objects.all()
    context = {
        'images' : images,
    }
    return render(request, 'rasmlar.html', context) 
def loyihalar(request):
    mavzu = Mavzu.objects.all()
    context = {
        'mavzu' : mavzu,
    }
    return render(request, 'loyihalar.html', context) 

def contact(request):
    if request.method == "POST":
        form = MyCommentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            messages.success(request, 'Xabaringiz muvafaqiyatli yuborildi!')
            return redirect('contact')
    else:
        form = MyCommentForm()
    return render(request, 'contact.html', {'form': form})         
