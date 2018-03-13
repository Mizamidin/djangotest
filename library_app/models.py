from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, help_text="Sanatty engiziniz")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"

class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        db_table = "author"

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "publisher"

class Book(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    isbn = models.CharField(max_length=20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
                                  related_name="books")
    authors = models.ManyToManyField(Author, related_name="books")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name="books")
    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
