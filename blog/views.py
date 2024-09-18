from django.shortcuts import render, get_object_or_404 
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    # queryset = Post.objects.all()
    # queryset = Post.objects.all().order_by("created_on")
    queryset = Post.objects.filter(status=1) # filter by status = 1 for those published posts
    template_name = "blog/index.html"
    paginate_by = 6


# Post detail view using function view
def post_detail(request, slug):
    ''' 
    Display and individual :model:`blog.Post`

    **Context**

    ``post``
        An instance of :model:`blog.Post`
    
    **Template:**

    :template:`blog/post_detail.html`

    '''
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )