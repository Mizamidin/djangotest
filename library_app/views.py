from django.shortcuts import render, get_object_or_404
from library_app.models import Category, Book, Publisher, Author
import datetime
# Create your views here.

def home(request):
    book_categories = Category.objects.all()
    time=datetime.datetime.now()
    n_hour=time.hour
    n_minute=time.minute
    n_second=time.second
    n_year=time.year
    n_month=time.month
    n_day=time.day
    w_day=time.weekday
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    

    return render(request, 'home.html', {'categories':book_categories, 'num_visits':num_visits,'hour':n_hour,'minute':n_minute,'second':n_second,'year':n_year,'month':n_month,'day':n_day,'weekday':w_day})
def logout(request):
    return render(request, 'logout.html')
def login(request):
    return render(request, 'login.html')

def book_list_in_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'library_app/books.html', {'category':category})