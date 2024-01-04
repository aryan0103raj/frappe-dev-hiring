from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    debt = models.PositiveSmallIntegerField(default=0)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    
    def isDebtOutstanding(self) -> bool:
        return self.debt >= 500
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'