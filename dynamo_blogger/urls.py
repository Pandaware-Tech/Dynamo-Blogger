from django.urls import path
from dynamo_blogger import views


app_name = "dynamo_blogger"


urlpatterns = [
    path("", views.home__page, name="home__page"),
    path("<slug>/", views.blog__post, name="blog__post"),
    path("category/<slug>/", views.category__page, name="category__page"),
]