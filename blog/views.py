from django.shortcuts import render
# Create your views here.


def blog(request):
    context= {
        'text': 'Blog Page',
        'year': 2025,
    }
    return render(
        request,
        'blog/index.html',
        context,
)

def example(request):
    context= {
        'text': 'Example Blog Page',
        'title': 'Ailton\'s Blog',
        'year': 2025,
    }    
    return render(
        request,
        'blog/example.html',
        context,
)