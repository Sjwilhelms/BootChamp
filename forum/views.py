from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Post, Profile

class PostList(generic.ListView):
    """
    Displays list of posts"
    """
    model = Post

class Profile(generic.ListView):
    model = Profile