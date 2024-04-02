from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    confirmation_code = models.CharField(max_length=10)

class Ad(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    content = models.FileField(upload_to='content/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=50)