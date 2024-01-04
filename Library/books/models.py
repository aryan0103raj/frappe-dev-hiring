from django.db import models

# Create your models here.

class Book(models.Model):
    bookID = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=300)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    isbn = models.CharField(max_length=10, unique=True)
    isbn13 = models.CharField(max_length=13, unique=True)
    language_code = models.CharField(max_length=10)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.DateField()
    publisher = models.CharField(max_length=100)
    stock = models.PositiveSmallIntegerField(default=1)

    def __str__(self) -> str:
        return f'{self.title} by {self.publisher}'
