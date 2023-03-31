from django.contrib import admin
from .models import Genre, Language, Author, Book, BookInstance

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.StackedInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


admin.site.register(Author, AuthorAdmin)


class BookInstanceInline(admin.TabularInline):
    """Make associated BookInstance editable while editing associated book"""
    model = BookInstance
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Inline editing of associated records Sometimes it can make sense to be able to add associated records at the
    same time. For example, it may make sense to have both the book information and information about the specific
    copies you've got on the same detail page """

    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'imprint', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )
