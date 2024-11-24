from django.db import models

class Header(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    text = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

class SocialMedia(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
class AboutUs(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images')
    address = models.TextField(null=True, blank=True)
    contacts = models.ManyToManyField(SocialMedia)
    def __str__(self):
        return self.text



class HoneySorts(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Facts(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.text
 
class Shop(models.Model):
    name = models.CharField(max_length=200)
    office = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Mission(models.Model):
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.text