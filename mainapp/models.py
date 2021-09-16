from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title

class Hometext(models.Model):
    title = models.CharField(max_length=150) 
    text = models.TextField()  

    def __str__(self):
        return self.title 

class About(models.Model):
    images = models.ImageField(upload_to='img/%y')
    title = models.CharField(max_length=100) 
    text = models.TextField()

    def __str__(self):
        return self.title   

class AboutText(models.Model):
    title = models.CharField(max_length=100) 
    text = models.TextField()

    def __str__(self):
        return self.title    

class Mavzu(models.Model):
    title = models.CharField(max_length=100) 
    text = models.TextField()

    def __str__(self):
        return self.title     

class Images(models.Model):
    title = models.CharField(max_length=100) 
    images = models.ImageField(upload_to='img/%y')
    text = models.TextField()

    def __str__(self):
        return self.title   
class Video(models.Model):
    title = models.CharField(max_length=150)
    video = models.FileField(upload_to='vedeo/%y')
    text = models.TextField()

    def __str__(self):
        return self.title   

class Contact(models.Model):
    name = models.CharField("First name", max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField("Phone number", max_length=15, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.name                                     