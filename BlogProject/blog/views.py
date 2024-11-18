from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm
# Create your views here.

def detail(request, category_slug,slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False) # will create temporary comment for us
            comment.post = post
            comment.save() # will save the comment in database
            
            return redirect('detail', slug=slug)
    else:
        form = CommentForm()
    context = {
        'post' : post,
        'form' : form
    }
    return render(request,'blog/detail.html',context)

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    context = {
        'category' : category,
        'posts': posts
    }
    return render(request,'blog/category.html',context )

def search(request):
    query = request.GET.get('query','')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query) ,status=Post.ACTIVE)
    context = {
    'posts' : posts,
    'query' : query # what user search
    }
    return render(request,'blog/search.html',context)
    
