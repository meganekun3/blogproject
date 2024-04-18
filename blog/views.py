from django.shortcuts import render
from django.views.generic import ListView, CreateView
from blog.models import Post

# Create your views here.
def toppage(request):
    return render(request,"index.html")

class PostList(ListView):
    model = Post
    template_name = "list.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "post.html"
    fields = ["title", "content"]