from django.utils.text import slugify
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth import get_user_model
from dynamo_blogger.helpers.timestamps import TimeStampedModel


User = get_user_model()


class Category(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    
    class Meta:
        verbose_name_plural = "Blog Categories"
        db_table = "blog_categories"
        
    def __str__(self) -> str:
        return self.slug
    
    def get_absolute_url(self):
        return reverse("dynamo_blogger:category__page", args=[self.slug])
    
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
            super(Category, self).save(*args, **kwargs)
        super(Category, self).save(*args, **kwargs)

    
class PostAuthor(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="author_images/", null=True, blank=True)
    biography = RichTextField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Blog Authors"
        db_table = "blog_authors"
    
    def __str__(self) -> str:
        return "{}'s author profile".format(self.user.username)
    
    def fullname(self) -> str:
        return "{} {}".format(self.user.first_name, self.user.last_name)
        

class Post(TimeStampedModel):
    STATUS_TYPES = (
        ("draft", "draft"),
        ("published", "published"),
        ("in-review", "in-review"),
        ("rejected", "rejected"),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True, editable=False)
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    tag = models.ForeignKey(Category, null=True, blank=True, on_delete=models.DO_NOTHING)
    description = RichTextField()
    featured = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_TYPES, default="draft")
    author = models.ForeignKey(PostAuthor, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Blog Posts"
        db_table = "blog_posts"
        
    def __str__(self) -> str:
        return "{}: {}".format(self.title, self.tag.slug)
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)
        super(Post, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("dynamo_blogger:blog__post", args=[self.slug])
         
    def get_number_of_comments(self):
        """
        It returns the number of comments associated with a post
        :return: The number of comments for a given post.
        """
        comment_count = Comment.objects.filter(blog_post_id=self.id).count()
        return comment_count
        
        
        
class Comment(TimeStampedModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    website = models.URLField(max_length=255)
    message = models.TextField(max_length=600)
    blog_post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
    reply_to = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name_plural = "Blog Comments"
        db_table = "blog_comments"
        
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super(Comment, self).save(*args, **kwargs)
    
