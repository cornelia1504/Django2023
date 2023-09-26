# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from libraryapp.models import Book
def vw_books(request, ):
    return render(request, "book_list.html", {"books": Book.objects.all()})
def vw_book2(request,):
    title = "Alice in wonderland"
    author = "Lewis carroll"
    description = "It is about a girl in a phantasy world"
    return render(request, "book.html", {"title" : title, "author" : author, "description" : description})

def vw_book3(request,bookid):
    title = "Alice in wonderland"
    author = "Lewis carroll"
    description = "It is about a girl in a phantasy world"
    return render(request, "book2.html", {"bookid" : bookid,"title" : title, "author" : author, "description" : description})


def vw_home(request):
    name = "Bogo"
    #html = "<html><body>Tongasoa! from {name}</body></html>".format(name=name)
    html = "<html><body>Tongasoa! Bienvenu à la bibliothèque</body></html>"
    return HttpResponse(html)

def vw_book(request):
    title = "Alice in wonderland"
    author = "Lewis carroll"
    description = "It is about a girl in a phantasy world"
    my_template = "<html><body><h1>{{ title }}</h1><h2>{{ author }}</h2><p>{{ description }}</p></body></html>"
    html = "<html><body><h1>ALice in wonderlande</h1><h2>Lewis carroll</h2><p>It is about a girl in a phantasy world</p></body></html>"
    return HttpResponse(html)