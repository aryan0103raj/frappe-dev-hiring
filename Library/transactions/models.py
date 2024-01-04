from django.db import models
from books.models import Book
from members.models import Member
import datetime

# Create your models here.
class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    rent_fee = models.PositiveSmallIntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.book.title} issued to {self.member.first_name} {self.member.last_name}'