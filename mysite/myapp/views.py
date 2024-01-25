from django.shortcuts import render

from django.http import HttpResponse 

from .forms import CalendarForm
#from .models import Book
# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def calendar(request):
    form =CalendarForm()
    return render(render, 'calendar.html', {'form': form})

'''
def book_by_id(request, book_id):
    book = Book.objects.get(pk = book_id)
    return render(request, 'book_detail.html', {'book':book})

#HttpResponse(f'Book: {book.title}, published on {book.pub_date}')
'''