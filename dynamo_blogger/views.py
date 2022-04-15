from django.shortcuts import render
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from dynamo_blogger.models import Category, Post, Comment


def home__page(request:HttpRequest) -> HttpResponse:
    """
    > It returns a rendered template of the home page, 
    with the site name, social media links, and
    categories
    
    :param request: This is the request object that Django passes to the view
    :type request: HttpRequest
    :return: A HttpResponse object.
    """
    
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


def blog__post(request:HttpRequest, slug:str) -> HttpResponse:
    """
    > The function `blog__post` takes a request and a slug, and returns a response
    
    :param request: The request object
    :type request: HttpRequest
    :param slug: The slug of the post to be displayed
    :type slug: str
    :return: A HttpResponse object.
    """
    
    post = Post.objects.get(slug=slug)
    
    categories = Category.objects.all().order_by("date_created")
    
    context = {
        "categories": categories,
        "post": post,
        
        "site__name": settings.DYNAMO_BLOGGER['site_name'],
        "facebook": settings.DYNAMO_BLOGGER['facebook'],
        "twitter": settings.DYNAMO_BLOGGER['twitter'],
        "linkedin": settings.DYNAMO_BLOGGER['linkedin'],
        "instagram": settings.DYNAMO_BLOGGER['instagram'],
    }
    return render(request, "blog/blog-post.html", context)


def category__page(request:HttpRequest, slug:str) -> HttpResponse:
    """
    > It gets the category from the database, 
    gets all the categories from the database, 
    and then renders the category page
    
    :param request: The request object
    :type request: HttpRequest
    :param slug: The slug of the category
    :type slug: str
    :return: A HttpResponse object.
    """
    
    category = Category.objects.get(slug=slug)
    
    categories = Category.objects.all().order_by("date_created")
    
    context = {
        "categories": categories,
        "category": category,
        
        "site__name": settings.DYNAMO_BLOGGER['site_name'],
        "facebook": settings.DYNAMO_BLOGGER['facebook'],
        "twitter": settings.DYNAMO_BLOGGER['twitter'],
        "linkedin": settings.DYNAMO_BLOGGER['linkedin'],
        "instagram": settings.DYNAMO_BLOGGER['instagram'],
    }
    return render(request, "blog/category.html", context)