from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, "blog/blog.html")

def posts_page(request):
    pass

def single_post(request, post: str):
    pass
