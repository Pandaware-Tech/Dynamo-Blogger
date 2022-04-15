from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from dynamo_blogger.models import Category, Post, Comment


def home__page(request:HttpRequest) -> HttpResponse:
    
    categories = Category.objects.all().order_by("date_created")
    
    context = {
        "site__name": settings.DYNAMO_BLOGGER['site_name'],
        "facebook": settings.DYNAMO_BLOGGER['facebook'],
        "twitter": settings.DYNAMO_BLOGGER['twitter'],
        "linkedin": settings.DYNAMO_BLOGGER['linkedin'],
        "instagram": settings.DYNAMO_BLOGGER['instagram'],
        
        "categories": categories
    }
    return render(request, "blog/index.html", context)


def blog__post(request:HttpRequest) -> HttpResponse:
    
    context = {}
    return render(request, "blog/blog-post.html", context)


def category__page(request:HttpRequest) -> HttpResponse:
    
    context = {}
    return render(request, "blog/category.html", context)