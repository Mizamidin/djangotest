from django.urls import path
from library_app import views

urlpatterns = [
    # path('all/', all_books, name = 'all_books')
    path('<int:pk>/', views.book_list_in_category, name = "book_list")
]