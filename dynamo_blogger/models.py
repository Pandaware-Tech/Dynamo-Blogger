from django.utils.text import slugify
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth import get_user_model
from dynamo_blogger.helpers.timestamps import TimeStampedModel


User = get_user_model()


class Category(TimeStampedModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Blog Categories"
        db_table = "blog_categories"
        
    def __str__(self) -> str:
        return self.slug
    
    def get_absolute_url(self):
        return reverse("category__page", kwargs={"slug": self.slug})
    
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
            super(Category, self).save(*args, **kwargs)
        super(Category, self).save(*args, **kwargs)
        
        

class Post(TimeStampedModel):
    STATUS_TYPES = (
        ("draft", "draft"),
        ("published", "published"),
        ("in-review", "in-review"),
        ("rejected", "rejected"),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    categories = models.ManyToManyField(Category, null=True, blank=True)
    description = RichTextField()
    featured = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_TYPES, default="draft")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Blog Posts"
        db_table = "blog_posts"
    
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)
        super(Post, self).save(*args, **kwargs)
        
    
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
    