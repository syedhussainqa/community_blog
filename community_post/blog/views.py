from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Syed',
        'title': 'New Story',
        'content': 'First story posted',
        'date_posted': 'January 1, 2019',
    },
    {
        'author': 'Sammy',
        'title': 'Sammy New Story',
        'content': 'Second story posted',
        'date_posted': 'March 1, 2019',
    }
]

# Create your views here.

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    #return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html')












    