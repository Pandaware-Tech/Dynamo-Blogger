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
    
    # Get latest updated posts
    latest_posts = Post.objects.filter(status="published").order_by("date_updated")[:2]
    
    # Get recent created posts
    recent_posts = Post.objects.filter(status="published").order_by("date_created")[:6]
    
    # Get categories title 
    category_names = []
    
    # Append each category name to category_names list
    [category_names.append(category.slug) for category in categories]
    
    # Print category names to the terminal
    print("Category Names: ", category_names)
    
    # Get posts with different categories
    posts_1 = Post.objects.filter(tag__slug=category_names[0], status="published").order_by("date_created")[:1]
    posts_2 = Post.objects.filter(tag__slug=category_names[1], status="published").order_by("date_created")[:2]
    posts_3 = Post.objects.filter(tag__slug=category_names[2], status="published").order_by("date_created")[:2]
    posts_4 = Post.objects.filter(tag__slug=category_names[3], status="published").order_by("date_created")[:2]
    
    # Get featured posts
    featured_posts = Post.objects.filter(featured=True, status="published").order_by("date_created")[:3]
    
    # Most read featured posts
    most_read_posts = Post.objects.filter(featured=True, status="published").order_by("date_created")[:4]
    
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