from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Comment


def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')

        if name and message:
            Comment.objects.create(name=name, message=message, post=post)

            return redirect(f"/blog/{slug}/#comments")
        

    return render(request, 'blog/detail.html', {"post": post})
