from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "judul" : "Ini Adalah Halaman About",
        "menu" : [
            ["/", "Home"],
            ["/blog", "Blog"],
            ["/about", "About"]
        ],
        "gambar" : "about/img/banner_about.png",
        "css_app" : "about/css/styles.css"
    }
    return render(request, 'about/index.html', context)