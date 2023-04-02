from django.shortcuts import render
from .models import Book, BookInstance, Author, Genre
from django.views import generic


# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_available_instances = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1



    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_available_instances': num_available_instances,
        'num_authors': num_authors,
        'num_visits':num_visits
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['Total_Books'] = 10
        return context

    paginate_by = 1
    template_name = 'book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorListView(generic.ListView):
    model = Author

    def get_queryset(self):
        return Author.objects.all()

    template_name = 'author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'

