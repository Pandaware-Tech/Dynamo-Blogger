from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from dynamo_blogger.models import Category, Newsletter, Post, Comment


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
    print("Category Names: ", category_names[2])
    
    # Get posts with different categories
    posts_1 = Post.objects.filter(tag__slug=category_names[0], status="published").order_by("date_created")[:1]
    posts_2 = Post.objects.filter(tag__slug=category_names[1], status="published").order_by("date_created")[:2]
    posts_3 = Post.objects.filter(tag__slug=category_names[2], status="published").order_by("date_created")[:2]
    posts_4 = Post.objects.filter(tag__slug=category_names[3], status="published").order_by("date_created")[:2]
    
    # Get featured posts
    featured_posts = Post.objects.filter(featured=True, status="published").order_by("date_created")[:3]
    
    # Most read featured posts
    most_read_posts = Post.objects.filter(featured=True, status="published").order_by("date_created")[:4]
    
    
    if request.method == "POST":
        email = request.POST.get("newsletter")
    
        # Create newsletter and save to database
        newsletter = Newsletter.objects.create(email=email)
        newsletter.save()
        
        # Redirect user to the home page with a response message
        messages.success(request, "You have been subscribed to our newsletter!")
        return redirect("dynamo_blogger:home__page")

    context = {
        "site__name": settings.DYNAMO_BLOGGER['site_name'],
        "facebook": settings.DYNAMO_BLOGGER['facebook'],
        "twitter": settings.DYNAMO_BLOGGER['twitter'],
        "linkedin": settings.DYNAMO_BLOGGER['linkedin'],
        "instagram": settings.DYNAMO_BLOGGER['instagram'],
        
        "latest_posts": latest_posts,
        "recent_posts": recent_posts,
        "posts_1": posts_1,
        "posts_2": posts_2,
        "posts_3": posts_3,
        "posts_4": posts_4,
        "featured_posts": featured_posts,
        "most_read_posts": most_read_posts,
        
        "categories": categories
    }
    return render(request, "blog/index.html", context)


def blog__post(request:HttpRequest, slug:str) -> HttpResponse:
    """
    > The function `blog__post` takes a request and a slug, 
    gets the most read posts, the category page and then renders them 
    to the home page (returns a response)
    
    :param request: The request object
    :type request: HttpRequest
    :param slug: The slug of the post to be displayed
    :type slug: str
    :return: A HttpResponse object.
    """
    
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        post = None
    
    # Get featured posts
    featured_posts = Post.objects.filter(featured=True, status="published")\
        .order_by("date_created")[:2]
    
    # Most read featured posts
    most_read_posts = Post.objects.filter(featured=True, status="published")\
        .order_by("date_created")[:4]
    
    # User comments 
    comments = Comment.objects.filter(blog_post=post)
    
    categories = Category.objects.all().order_by("date_created")
    
    context = {
        "categories": categories,
        "post": post,
        
        "featured_posts": featured_posts,
        "most_read_posts": most_read_posts,
        
        "comments": comments,
        
        "site__name": settings.DYNAMO_BLOGGER['site_name'],
        "facebook": settings.DYNAMO_BLOGGER['facebook'],
        "twitter": settings.DYNAMO_BLOGGER['twitter'],
        "linkedin": settings.DYNAMO_BLOGGER['linkedin'],
        "instagram": settings.DYNAMO_BLOGGER['instagram'],
    }
    return render(request, "blog/blog-post.html", context)


def category__page(request:HttpRequest, slug:str) -> HttpResponse:
    """
    It gets the category from the database, 
    gets all the posts that belong to that category, gets the
    most read posts, the category page and then renders them 
    to the category page
    
    :param request: The request object
    :type request: HttpRequest
    :param slug: The slug of the category to be displayed
    :type slug: str
    :return: A HttpResponse object
    """

    category = Category.objects.get(slug=slug)
    
    categories = Category.objects.all().order_by("date_created")
    
    # Category posts
    posts = Post.objects.filter(tag=category, status="published")\
        .order_by("date_created")
    
    try:
        featured_post = Post.objects.get(tag=category, status="published", featured=True)
    except Post.DoesNotExist:
        featured_post = Post.objects.filter(tag=category, status="published").first()
        
    # Most read featured posts
    most_read_posts = Post.objects.filter(featured=True, status="published")\
        .order_by("date_created")[:4]
    
    
    context = {
        "categories": categories,
        "category": category,
        
        "most_read_posts": most_read_posts,
        "posts": posts,
        "featured_post": featured_post,
        
        "site__name": settings.DYNAMO_BLOGGER['site_name'],
        "facebook": settings.DYNAMO_BLOGGER['facebook'],
        "twitter": settings.DYNAMO_BLOGGER['twitter'],
        "linkedin": settings.DYNAMO_BLOGGER['linkedin'],
        "instagram": settings.DYNAMO_BLOGGER['instagram'],
    }
    return render(request, "blog/category.html", context)


def create__comment(request:HttpRequest, slug) -> HttpResponseRedirect:
    """
    > Create a comment object with the data from the form, 
    save it to the database, and redirect the
    user to the blog post page
    
    :param request: The request object that was sent to the view
    :type request: HttpRequest
    :param slug: The slug of the blog post that the comment is being created for
    :return: A redirect to the blog post page.
    """
    name = request.POST.get("name")
    email = request.POST.get("email")
    website = request.POST.get("website")
    message = request.POST.get("message")
    
    # Create comment and save to database
    comment = Comment.objects.create(
        name=name, email=email, website=website, 
        message=message, blog_post=Post.objects.get(slug=slug)
    )
    comment.save()
    return redirect("dynamo_blogger:blog__post", slug)
