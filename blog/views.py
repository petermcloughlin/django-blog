from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    # queryset = Post.objects.all()
    # queryset = Post.objects.all().order_by("created_on")
    queryset = Post.objects.filter(status=1) # filter by status = 1 for those published posts
    template_name = "post_list.html"
