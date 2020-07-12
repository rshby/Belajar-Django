
##==== Views Blog ===

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #=> index untuk si blog
    context = {
        "judul" : "Halaman Blog Website",
        "coder" : "Reo Sahobby",
        "menu" : [
            ["/","Home"],
            ["/blog","Blog"],
            ["/about", "About"],
            ["/blog/recent","Recent"],
            ["/blog/profile","Profile"]
        ],
        "gambar" : "blog/img/banner_blog.png"
    }
    return render(request, 'blog/index.html', context)

def recent(request):
    context = {
        "judul" : "Halaman Recent Apps",
        "coder" : "Reo S",
        "menu" : [
            ["/blog","Blog"],
            ["/blog/profile", "Profile"]
        ],
        "gambar" : "blog/img/banner_blog.png"
    }
    return render(request, 'blog/index.html', context)

def profile(request):
    context = {
        "judul" : "Halaman Profil Penulis",
        "coder" : "Reo Sahobby",
        "alamat" : "Klaten",
        "menu" : [
            ["/blog","Blog"],
            ["/blog/recent", "Recent"]
        ],
        "gambar" : "blog/img/banner_blog.png"
    }
    return render(request, 'blog/index.html', context)