
##==== Views Blog ===

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): #=> index untuk si blog
    context = {
        "judul" : "Halaman Blog Website",
        "coder" : "Reo Sahobby"
    }
    return render(request, 'blog/index.html', context)

def recent(request):
    context = {
        "judul" : "Halaman Recent Apps",
        "coder" : "Reo S",
    }
    return render(request, 'blog/index.html', context)

def profile(request):
    context = {
        "judul" : "Halaman Profil Penulis",
        "coder" : "Reo Sahobby",
        "alamat" : "Klaten"
    }
    return render(request, 'blog/index.html', context)