from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Group, Post
from .utils import paginator_function

User = get_user_model()


@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return redirect('posts:profile', request.user.username)
    else:
        return render(request, 'posts/create_post.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user != post.author:
        return redirect('posts:post_detail', pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts:post_detail', pk)
    else:
        return render(request,
            'posts/create_post.html', {'form': form, 'is_edit': True}
        )


def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = author.posts.all()
    context = {
        'author': author,
        'posts': posts,
        'page_obj': paginator_function(posts, request),
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'posts/post_detail.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
        'page_obj': paginator_function(posts, request),
    }

    return render(request, 'posts/group_list.html', context)


def index(request):
    posts = Post.objects.all()
    context = {
        'page_obj': paginator_function(posts, request),
    }
    return render(request, 'posts/index.html', context)
