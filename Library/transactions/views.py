from django.shortcuts import render, redirect
from .models import *
from books.models import *
from members.models import *
from django.db.models import Q
from datetime import datetime

# Create your views here.

def get_transactions(request):
    available_books = Book.objects.filter(stock__gt = 0)
    valid_members = Member.objects.filter(debt__lt = 500)
    open_transactions = Transaction.objects.filter(return_date = None)
    
    context = { 
        'transactions': Transaction.objects.all(),
        'available_books': available_books,
        'valid_members': valid_members,
        'open_transactions': open_transactions,
    }

    return render(request, 'transactions/transaction_list.html', context)

def issue_book(request):
    book = Book.objects.filter(bookID=request.POST['bookID']).first()
    member = Member.objects.filter(email=request.POST['email']).first()

    book.stock -= 1
    member.debt += int(request.POST['rent'])

    transaction = Transaction(
        book=book,
        member=member,
        rent_fee=int(request.POST['rent'])
    )

    book.save()
    member.save()
    transaction.save()

    return redirect('/transactions/')

def return_book(request):
    bookID, email = request.POST['transactionID'].split("-")
    book = Book.objects.filter(bookID=bookID).first()
    member = Member.objects.filter(email=email).first()

    transaction = Transaction.objects.filter(
        Q(book=book) &
        Q(member=member)
    ).first()

    book.stock += 1
    member.debt -= transaction.rent_fee
    transaction.return_date = datetime.now().strftime("%Y-%m-%d")

    book.save()
    member.save()
    transaction.save()

    return redirect('/transactions/')