from django.contrib import admin
from .models import Book

# Custom admin configuration
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'available')
    list_filter = ('publication_year', 'available', 'genre') 
    search_fields = ('title', 'author')  

admin.site.register(Book)
