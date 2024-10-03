from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(default=timezone.now() + timedelta(days=7))

    def __str__(self):
        return f'{self.book.title} rented by {self.user.username}'
