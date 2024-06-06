from django.db.models import Q

from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Comment, Category


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')

        if name and message:
            Comment.objects.create(name=name, message=message, post=post)

            return redirect(f"/blog/{slug}/#comments")
        

    return render(request, 'blog/detail.html', {"post": post})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)

    return render(request, 'blog/category.html', {'category': category, 'posts': posts})


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'blog/search.html', {'query': query, 'posts': posts})