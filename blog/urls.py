from . import views
from django.urls import path


urlpatterns = [
    path("", views.home_page),
    path("posts/", views.posts_page),
    path("posts/<str:post>, views.single_post")
]