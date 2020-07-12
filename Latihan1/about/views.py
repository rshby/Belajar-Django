from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "judul" : "Ini Adalah Halaman About",
        "nav" : [
            ["/", "Home"],
            ["/blog", "Blog"],
            ["/about", "About"]
        ],
        "gambar" : "about/img/banner_about.png",
        "css_app" : "about/css/css_about.css"
    }
    return render(request, 'about/index.html', context)