from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Post


def index(request):
    latest_posts = Post.objects.order_by('-created')[:10]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog/index.html', context)


def detail(request, slug):
    """Post Detail

    This is the main view for a given post.
    """
    try:
        post = Post.objects.get(slug__contains=slug)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    return render(request, 'blog/detail.html', {'post': post})
