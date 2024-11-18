from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    context = {
        'posts' : posts
    }
    return render(request,'core/frontpage.html', context)


def about(request):
    name = 'Mohammad Shahbaz Alam'
    job_profile = 'Python Developer and Data Scientist'
    context = {
    'name' : name,
    'job' : job_profile
    }
    return render(request,'core/about.html',context)


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type='text/plain')