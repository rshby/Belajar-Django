from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #=> index untuk si blog
    return render(request, 'blog/blog.html')

def recent(request):
    return HttpResponse('<h1>ini adalah recent post</h1>')
