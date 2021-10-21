from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('filled-login/', filled_index, name='filled-login'),  # remove later
    path('filled-contacts/', filled_contacts, name='filled-contacts'),  # remove later
    path('men/', men, name='men'),
    path('women/', women, name='women'),
    path('contacts/', contacts, name='contacts'),
    path('login/', login, name='login'),
    path('signup/', signup, name='singup'),
    path('about-project/', about_project, name='about-project'),
    path('about-members/', about_members, name='about-members'),
    path('member-contacts', member_contacts, name='member-contacts'),
]
