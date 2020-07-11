from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "judul" : "Ini Adalah Halaman About",
        "menu" : [
            ["/", "Home"],
            ["/blog", "Blog"],
            ["/about", "About"]
        ]
    }
    return render(request, 'about/index.html', context)