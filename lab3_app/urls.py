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
    path('member-contacts/', member_contacts, name='member-contacts'),
    path('form-shoes/', add_shoes, name='add-shoes'),
    path('all-shoes/', all_shoes, name='all-shoes'),
    path('update_shoes/<str:pk>/', update_shoes, name="update_shoes"),
    path('delete_shoes/<str:pk>/', delete_shoes, name="delete_shoes"),
    path('bootstrap/index', boot_index, name='boot-index'),
    path('bootstrap/men', boot_men, name='boot-men'),
    path('bootstrap/women', boot_women, name='boot-women'),
    path('bootstrap/contacts', boot_contacts, name='boot-contacts'),
    path('bootstrap/login', boot_login, name='boot-login'),
    path('bootstrap/signup', boot_signup, name='boot-signup'),
]
