from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home__page(request:HttpRequest) -> HttpResponse:
    
    context = {}
    return render(request, "blog/index.html", context)


def blog__post(request:HttpRequest) -> HttpResponse:
    
    context = {}
    return render(request, "blog/blog-post.html", context)