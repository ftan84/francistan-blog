from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    latest_posts = Post.objects.order_by('-created')[:10]
    output = '</br>'.join([
        ' | '.join([post.title, post.author.first_name])
        for post in latest_posts])
    return HttpResponse(output)


def detail(request, slug):
    """Post Detail

    This is the main view for a given post.
    """
    return HttpResponse(slug)
