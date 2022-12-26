from django.shortcuts import render
from blogpost.models import NewPost
# Create your views here.
def Home(request):
    all_posts = NewPost.objects.all()
    data = {
        "all_posts": all_posts
    }
    return render(request,"index.html",data)

def Post(request,id):
    current_post = NewPost.objects.get(id=id)
    data = {
        "current_post": current_post
    }
    return render(request,"post.html",data)

def Author(request):
    return render(request,"author.html")