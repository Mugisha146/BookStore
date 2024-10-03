from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Rental
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.mail import send_mail
import datetime

def book_list(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'books/book_list.html', {'books': books})  # Adjust the template path accordingly

@login_required
def rent_book(request, title):
    book = get_object_or_404(Book, title=title)  # Fetch book using title
    rental = Rental.objects.create(user=request.user, book=book)
    book.available = False
    book.save()
    print(f"Book rented successfully: {book.title}")
    send_mail(
        'Book Rented',
        f'You rented {book.title}. Please return it by {rental.due_date}.',
        'emmyzizo1@gmail.com',
        [request.user.email],
        fail_silently=False,
    )
    messages.success(request, f"You successfully rented '{book.title}'. Check your email for details.")
    return redirect('book_list')


@login_required
def return_book(request, title):
    # Filter active rentals and pick the earliest one
    rental = Rental.objects.filter(book__title=title, user=request.user, return_date__isnull=True).order_by('rental_date').first()
    
    if rental:
        rental.return_date = timezone.now()
        rental.save()
        
        rental.book.available = True
        rental.book.save()

        send_mail(
            'Book Returned',
            f'Thank you for returning {rental.book.title}.',
            'emmyzizo1@gmail.com',
            [request.user.email],
            fail_silently=False,
        )

        messages.success(request, f"You successfully returned '{rental.book.title}'.")
    else:
        messages.error(request, "No active rentals found for this book.")
    
    return redirect('book_list')



from .forms import BookForm
from django.core.exceptions import PermissionDenied

ADMIN_EMAIL = 'emmyzizo1@gmail.com'  # Set your admin email here

@login_required
def add_book(request):
    if request.user.email != ADMIN_EMAIL:
        raise PermissionDenied("You do not have permission to add books.")
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after saving
    else:
        form = BookForm()
    
    return render(request, 'books/add_book.html', {'form': form})

# books/views.py

from django.shortcuts import get_object_or_404

@login_required
def delete_book(request, title):
    if request.user.email != ADMIN_EMAIL:
        raise PermissionDenied("You do not have permission to delete books.")
    
    book = get_object_or_404(Book, title=title)  # Fetch book using title
    book.delete()
    return redirect('book_list')  # Redirect to book list after deletion

