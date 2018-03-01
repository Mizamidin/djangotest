from django.shortcuts import render
from library_app.models import Category, Book, Publisher, Author
# Create your views here.

def home(request):
    book_categories = Category.objects.all()
    return render(request, 'home.html', {'categories':book_categories})