from django.db import models

# Create your models here.

class Blogs(models.Model):
    heading = models.CharField(max_length=200)
    content = models.CharField(max_length=200, default='')
    image=models.FileField(upload_to = 'images/', null=True, blank=True)
    underheading = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)

    def __str__(self):
        return self.heading

class Post(models.Model):
    image=models.FileField(upload_to = 'images/', null=True, blank=True)

class Projects(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, default='')
    imagelink = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name