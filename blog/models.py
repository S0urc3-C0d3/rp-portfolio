from django.db import models
from django import forms

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=225)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    tags = models.ManyToManyField("Tag", related_name="posts")

    def __str__(self):
        return "Post: " + self.title

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "Category: " + self.name

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)

class Tag(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)

    def __str__(self):
        return self.name