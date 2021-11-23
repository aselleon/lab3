from django.shortcuts import render, redirect
from lab3_app.crud import *
from .forms import *


# Create your views here.

def index(request):
    return render(request, "lab3/html&css/index.html")


def all_shoes(request):
    shoes = Shoes.objects.all()
    context = {
        'shoes': shoes
    }
    return render(request, 'lab3/html&css/all_shoes.html', context=context)


def add_shoes(request):
    if request.method == 'POST':
        form = AddShoesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddShoesForm()

    return render(request, 'lab3/html&css/form-input-shoes.html', {"form": form})


def update_shoes(request):
    if request.method == 'POST':
        form = UpdateShoesForm(request.POST, request.FILES)


def men(request):
    shoes = get_all_men_shoes()
    data = {"shoes": shoes}
    return render(request, "lab3/html&css/men.html", context=data)


def women(request):
    shoes = get_all_women_shoes()
    data = {"shoes": shoes}
    return render(request, "lab3/html&css/women.html", context=data)


def contacts(request):
    return render(request, "lab3/html&css/contacts.html")


def login(request):
    return render(request, "lab3/html&css/login.html")


def signup(request):
    return render(request, "lab3/html&css/signup.html")


def filled_index(request):
    data = {"login": "Temirlan"}
    return render(request, "lab3/html&css/filled-login.html", context=data)


def filled_contacts(request):
    login = "Muslimov"
    email = ["example@gmail.com", "temirlan.muslimov.1@gmail.com"]
    address = ("Dostyk avenue 47", 'Al-Farabi 129')
    phone = ["+7 777 77 77", "+7 800 555 35 35"]
    data = {"login": login, "email": email, "address": address, "phone": phone}
    return render(request, "lab3/html&css/filled-contacts.html", context=data)


def about_project(request):
    return render(request, 'lab3/html&css/about-project.html')


def about_members(request):
    Tima = {"name": "Temirlan",
            "surname": "Muslimov",
            'age': 20,
            'specialty': 'Software engineering',
            'about': 'Future android <div>eloper',
            'url': "https://memepedia.ru/wp-content/uploads/2017/05/%D0%BA%D0%BE%D1%82-%D0%BF%D0%B8%D0%B0%D0%BD%D0%B8%D1%81%D1%82.jpg"}

    Daurbek = {"name": "Daurbek",
               "surname": "Sakhtarov",
               'age': 20,
               'specialty': 'Software engineering',
               'about': 'HTML HACKER',
               'url': 'https://avatars.githubusercontent.com/u/61458120?v=4'}
    data = {"members": (Tima, Daurbek)}
    return render(request, 'lab3/html&css/about-members.html', context=data)


def member_contacts(request):
    Tima = {"phone": "+7 707 619 28 78",
            "email": "temirlan.muslimov.1@gmail.com",
            "address": "Aksay-2"}
    Daurbek = {"phone": "+7 778 911 58 35",
               "email": "example@gmail.com",
               "address": "Varlamova"}
    data = {"members": (Tima, Daurbek)}
    return render(request, 'lab3/html&css/member-contacts.html', context=data)


def boot_index(request):
    return render(request, "lab3/bootstrap/index_boot.html")


def boot_men(request):
    shoes = [
        Shoe("shoe1", "100$", [40, 41, 42], "shoe1.png"),
        Shoe("shoe2", "130$", [42, 43, 45], "shoe2.png"),
        Shoe("shoe3", "120$", [40, 43, 44], "shoe3.png"),
        Shoe("shoe4", "140$", [40, 41, 42, 43, 45], "shoe4.png"),
        Shoe("shoe5", "124$", [40], "shoe5.png"),
        Shoe("shoe6", "129$", [40, 41], "shoe6.png"),
    ]
    data = {"shoes": shoes}
    return render(request, "lab3/bootstrap/men_boot.html", context=data)


def boot_women(request):
    shoes = [
        Shoe("shoe7", "100$", [40, 41, 42], "shoe7.png"),
        Shoe("shoe8", "130$", [42, 43, 45], "shoe8.png"),
        Shoe("shoe9", "120$", [40, 43, 44], "shoe9.png"),
        Shoe("shoe10", "140$", [40, 41, 42, 43, 45], "shoe10.png"),
        Shoe("shoe11", "124$", [40], "shoe11.png"),
        Shoe("shoe12", "129$", [40, 41], "shoe12.png"),
    ]
    data = {"shoes": shoes}
    return render(request, "lab3/bootstrap/women_boot.html", context=data)


def boot_contacts(request):
    login = "Muslimov"
    email = ["example@gmail.com", "temirlan.muslimov.1@gmail.com"]
    address = ("Dostyk avenue 47", 'Al-Farabi 129')
    phone = ["+7 777 77 77", "+7 800 555 35 35"]
    data = {"login": login, "email": email, "address": address, "phone": phone}
    return render(request, "lab3/bootstrap/contacts_boot.html", context=data)


def boot_login(request):
    return render(request, "lab3/bootstrap/login_boot.html")


def boot_signup(request):
    return render(request, "lab3/bootstrap/signup_boot.html")
