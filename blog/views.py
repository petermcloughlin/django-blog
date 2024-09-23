from django.shortcuts import render, get_object_or_404 
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import CommentForm
from django.contrib.auth.models import User

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
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        print('Received a POST request')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()  
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    print('About to render the template')

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,  
            "comment_form": comment_form,      
        }, # This dictionary is referred to as a context
    )
    # Another way of creating your context
    # context = {"post": post}
    # return render(
    #     request,
    #     "blog/post_detail.html",
    #     context
    # )

# Get Users comments
def profile_page(request):
    user =  get_object_or_404(User, user=request.user)
    # retrieve all comments by the user
    comments = user.commenter.all()