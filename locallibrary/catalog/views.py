from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre


# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_available_instances = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_available_instances': num_available_instances,
        'num_authors': num_authors
    }

    return render(request, 'index.html', context=context)
