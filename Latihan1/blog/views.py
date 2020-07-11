from django.shortcuts import render

# Create your views here.
def index(request): #=> index untuk si blog
    return render(request, 'blog.html')
