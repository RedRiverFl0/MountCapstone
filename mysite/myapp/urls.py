
from django.urls import path
from django.conf.urls.static import static

from .import views #connect this to the views
'''
urlpatterns = [
    path('', views.index, name = 'index'),
    path('book/<int:book_id>', views.book_by_id, name = 'book_by_id'),
]
'''

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('app/contact/post', views.calendar, name='calendar'),
    path('task/', views.task , name='task') #link to form to see what the task will be
]