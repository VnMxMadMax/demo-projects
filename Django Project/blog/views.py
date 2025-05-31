from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Post, Comment
from blog.forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import PostForm
from .models import Category
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.shortcuts import get_object_or_404

def blog_index(request):
    posts = Post.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_at")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm()
    }

    return render(request, "blog/detail.html", context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "blog/register.html", {"form": form})

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            # Add selected existing categories
            form.save_m2m()
            
            # Handle new category
            new_cat_name = form.cleaned_data.get('new_category')
            if new_cat_name:
                new_cat, created = Category.objects.get_or_create(name=new_cat_name)
                post.categories.add(new_cat)
            
            return redirect('blog_index')
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})

@login_required
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': post.total_likes()})

@csrf_exempt  # Optional if using JS CSRF token
@require_POST
def submit_comment(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        author = request.POST.get("author")
        body = request.POST.get("body")
        if author and body:
            Comment.objects.create(post=post, author=author, body=body)
            comment_count = post.comment_set.count()
            return JsonResponse({"status": "ok", "comment_count": comment_count})
        else:
            return JsonResponse({"status": "error", "message": "Missing fields"}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)