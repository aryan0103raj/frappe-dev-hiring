from django.shortcuts import render, redirect
from .models import *
import time
from django.db.models import Q
import requests
import math
from datetime import datetime
import json

# Create your views here.

def get_books(request):
    if request.method == 'POST':
        url = 'https://frappe.io/api/method/frappe-library'
        params = {}

        params['title'] = request.POST['title']
        params['authors'] = request.POST['authors']
        params['isbn'] = request.POST['isbn']
        params['publisher'] = request.POST['publisher']
        total_requests = math.ceil(int(request.POST['count'])/20.0)

        cnt = 0
        for i in range(1, total_requests + 1):
            params['page'] = i
            response = requests.get(url, params=params)
            parsed_data = json.loads(response.text)

            for book in parsed_data['message']:
                new_book = Book(
                    bookID = book['bookID'],
                    title = book['title'],
                    authors = book['authors'],
                    publisher = book['publisher'],
                    average_rating = book['average_rating'],
                    isbn = book['isbn'],
                    isbn13 = book['isbn13'],
                    language_code = book['language_code'],
                    ratings_count = book['ratings_count'],
                    num_pages = book['  num_pages'],
                    text_reviews_count = book['text_reviews_count'],
                    publication_date = datetime.strptime(book['publication_date'], '%m/%d/%Y').strftime('%Y-%m-%d'),
                    stock = 1,
                )

                queryset = Book.objects.filter(
                    Q(bookID=book['bookID']) |
                    Q(isbn=book['isbn']) |
                    Q(isbn13=book['isbn13'])
                )

                if queryset.count() == 0:
                    cnt += 1
                    new_book.save()
                
                if cnt == int(request.POST['count']):
                    break
        
        context = { 
            'books': Book.objects.all(),
            'title': '',
            'authors': '',
            'publisher': '',
            'isbn': '',
        }
        return render(request, 'books/book_list.html', context)

    title = request.GET.get('title', '')
    authors = request.GET.get('authors', '')
    publisher = request.GET.get('pusblisher', '')
    isbn = request.GET.get('isbn', '')

    queryset = Book.objects.filter(
        Q(title__icontains=title) &
        Q(authors__icontains=authors) &
        Q(publisher__icontains=publisher) &
        Q(isbn__icontains=isbn)
    )

    context = { 
        'books': queryset,
        'title': title,
        'authors': authors,
        'publisher': publisher,
        'isbn': isbn,
    }
    return render(request, 'books/book_list.html', context)

def delete_book(request, bookID):
    queryset = Book.objects.get(bookID=bookID)
    queryset.delete()
    time.sleep(1)
    return redirect('/books/')

def update_book(request, bookID):
    if request.method == 'POST':
        queryset = Book.objects.get(bookID=bookID)
        data = request.POST
        stock = data.get('stock')
        queryset.stock = stock
        queryset.save()
        return redirect('/books/')

    queryset = Book.objects.get(bookID=bookID)
    context = { 'book': queryset }
    return render(request, 'books/update_book.html', context)