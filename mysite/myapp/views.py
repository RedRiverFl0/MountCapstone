from django.shortcuts import render, redirect

from django.http import HttpResponse 

from .forms import CalendarForm
from .models import Person
from .forms import PersonForm
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html', {})  

def about(request):
    return render(request, 'about.html')



def calendar(request):
    form =CalendarForm()
    return render(request, 'calendar.html', {'form': form})

def account(request):
    all_person = Person.objects.all    #gets all of the people from the Person table
    return render(request, 'account.html', {'all':all_person})  #code that allows to input data through the name of 'all'

def task(request):
    if request.method == "POST":    
        form = PersonForm(request.POST or None)   #if form was submitted then store it under form variable
        if form.is_valid(): 
            form.save()         # if the form is valid then save it

        else: #if the form is not valid save all that was entered in the fields
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            email = request.POST['email']
            Pword = request.POST['Pword']

            messages.success(request, ('There was an error in your responce, Try again.')) #spit out this responce

            return render(request, 'task.html', {  #save all of the save variables in a dictionary
                'firstName':firstName,
                'lastName':lastName,
                'email':email,
                'Pword':Pword
            })

        messages.success(request, ('Your form has been submited and will be reviewed as soon as possible!'))
        return redirect('task') #display the form page

    else:
        return render(request, 'task.html', {}) #display the page even if the form isn't submitted

'''
def book_by_id(request, book_id):
    book = Book.objects.get(pk = book_id)
    return render(request, 'book_detail.html', {'book':book})

#HttpResponse(f'Book: {book.title}, published on {book.pub_date}')


all_person = Person.objects.all
    return render(request, 'task.html', {'all':all_person})
'''