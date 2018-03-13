from django.shortcuts import render, get_object_or_404
from library_app.models import Category, Book, Publisher, Author
# Create your views here.

def home(request):
    book_categories = Category.objects.all()
    return render(request, 'home.html', {'categories':book_categories})
def logout(request):
    return render(request, 'logout.html')
def login(request):
    return render(request, 'login.html')

def book_list_in_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'library_app/books.html', {'category':category})