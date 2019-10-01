from django.shortcuts import render
from blog.models import Post, Comment, Category
from blog.forms import CommentForm, PostForm, AddCategory
import requests

# Create your views here.
def blog_index(request):

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(
                author=form.cleaned_data["author"],
                title = form.cleaned_data["title"],
                body= form.cleaned_data["body"],
                category= form.cleaned_data["category"],
                tags =form.cleaned_data["tags"]
            )
            post.save()
    # include open weather api
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f213acc6b9f0f54e993ce23a6a61eb61'
    city = "Berlin"
    city_weather = requests.get(url.format(city)).json()

    weather = {"city": city,
               "temperature": city_weather["main"]["temp"],
               "description": city_weather["weather"][0]["description"],
               "icon": city_weather["weather"][0]["icon"]
               }

    posts = Post.objects.all().order_by("-created_on")
    context = {"posts": posts,
               "form" : form,}
    return render(request, "blog_index.html", context)

def blog_list_categories(request):

    form = AddCategory()
    if request.method == 'POST':
        form = AddCategory(request.POST)
        if form.is_valid():
            category = Category(
                name=form.cleaned_data["name"],
            )
            category.save()
    categories = Category.objects.all()
    context = {"categories":categories, "form":form}

    return render(request, "blog_list_categories.html", context=context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments":comments, "form":form}
    return render(request, "blog_detail.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    context = {"posts": posts}
    return render(request, "blog_category.html", context)

def change_category(request, category):

    category = Post.objects.filter(categories__name__contains=category)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
