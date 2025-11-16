from typing import Any

from blog.data import posts
from django.http import HttpRequest, Http404
from django.shortcuts import render
# Create your views here.


def blog(request):
    context = {
        # 'text': 'Blog Page',
        'posts': posts,
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def post(request: HttpRequest, post_id:int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    if found_post is None:
        raise Http404('Post não existe.')

        
    context= {
        # 'text': 'Blog Page',
        'post': found_post,
        'title': found_post['title'] + ' - ',
    }
    
    return render(
        request,
        'blog/post.html',
        context,
)


def example(request):
    context = {
        'text': 'Example Blog Page',
        'title': 'Site do Ailton',
    }
 
    return render(
        request,
        'blog/example.html',
        context,
)