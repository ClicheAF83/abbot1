from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'CLicheAF',
        'title' : 'monkey',
        'content' : 'content 1, is a lot. Check me out',
        'date_posted' : 'August 27, 2003'
    },
    {
        'author' : 'molybdenum',
        'title' : 'cat',
        'content' : 'Sleeping a lot. someone needs to wake me up',
        'date_posted' : 'August 27, 2003'

    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title': 'about'})

# Create your views here.
