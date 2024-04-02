from django.shortcuts import render, redirect

from django.http import HttpResponse,Http404 
from django.conf import settings
from .forms import CalendarForm
from .models import Person
from .forms import PersonForm
from .models import Hire
from .forms import HireForm

from django.core.files.storage import FileSystemStorage

from django.contrib import messages

import os


# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html', {})  

def about(request):
    return render(request, 'about.html')

def newJobs(request):
    
    return render(request, 'newJobs.html')

def oppertunities(request):
    findFile = request.POST.get('choice')

    goto = os.path.join(settings.MEDIA_ROOT, 'jobs', f'{findFile}')

    try:
        with open(goto, 'rb') as pdfFile:
            responce = HttpResponse(pdfFile.read(), content_type="application/pdf")
            responce['Content-Disposition'] = f'attachment; filename="{findFile}"'
            return responce
    except FileNotFoundError:
        raise Http404(f"{findFile} is not found")

def services(request):
    return render(request, 'services.html')

def calendar(request):
    form =CalendarForm()
    return render(request, 'calendar.html', {'form': form})

def account(request):
    all_person = Person.objects.all    #gets all of the people from the Person table
    all_hire = Hire.objects.all
    return render(request, 'account.html', {'all_P':all_person, 'all_H':all_hire })  #code that allows to input data through the name of 'all'

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
    
def hire(request):
    if request.method == "POST":    
        form = HireForm(request.POST or None, request.FILES)   #if form was submitted then store it under form variable
        if form.is_valid(): 
            
            form.save()         # if the form is valid then save it

        else: #if the form is not valid save all that was entered in the fields
            firstName = request.POST['firstName']
            lastName = request.POST['lastName']
            email = request.POST['email']
            

            messages.success(request, ('There was an error in your responce, Try again.')) #spit out this responce

            return render(request, 'hire.html', {  #save all of the save variables in a dictionary
                'firstName':firstName,
                'lastName':lastName,
                'email':email,
                
            })

        messages.success(request, ('Your form has been submited and will be reviewed as soon as possible!'))
        return redirect('hire') #display the form page

    else:
        return render(request, 'hire.html', {}) #display the page even if the form isn't submitted


