"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from members.views import *
from books.views import *
from transactions.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('delete-book/<bookID>', delete_book, name="delete_book"),
    path('update-book/<bookID>', update_book, name="update_book"),
    path('members/', get_members, name='get_members'),
    path('update-member/<id>', update_member, name="update_member"),
    path('delete-member/<id>', delete_member, name="delete_member"),
    path('transactions/', get_transactions, name='get_transactions'),
    path('issue-book/', issue_book, name="issue_book"),
    path('return-book/', return_book, name="return_book"),
    path('', RedirectView.as_view(url='books/')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
