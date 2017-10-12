from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from api.models import Book


def index(request):
    book_name = request.data.get('book_name')
    Book.objects.create(title=book_name)
    return HttpResponse("Hello, world. You're at the polls index.")