from django.shortcuts import render


def home(request):
    return render(
        request,
        'home/index.html',
        {
            'text': 'Home Page',
            'year': 2025,
        },
                  

)