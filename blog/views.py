from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hey')


def detail(request, slug):
    """Post Detail

    This is the main view for a given post.
    """
    return HttpResponse(slug)
