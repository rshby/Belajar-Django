from django.shortcuts import render

def index(request):
    context = {
        "judul" : "Halaman Home",
        "nav" : [
            ["/", "Home"],
            ["/blog", "Blog"],
            ["/about", "About"]
        ]
    }
    return render(request, 'index.html', context)