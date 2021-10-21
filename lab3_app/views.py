from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "lab3/index.html")


def men(request):
    return render(request, "lab3/htmls/men.html")


def women(request):
    return render(request, "lab3/htmls/women.html")


def contacts(request):
    return render(request, "lab3/htmls/contacts.html")


def login(request):
    return render(request, "lab3/htmls/login.html")


def signup(request):
    return render(request, "lab3/htmls/signup.html")


def filled_index(request):
    data = {"login": "Temirlan"}
    return render(request, "lab3/filled-login.html", context=data)


def filled_contacts(request):
    login = "Muslimov"
    email = ["example@gmail.com", "temirlan.muslimov.1@gmail.com"]
    address = ("Dostyk avenue 47", 'Al-Farabi 129')
    phone = ["+7 777 77 77", "+7 800 555 35 35"]
    data = {"login": login, "email": email, "address": address, "phone": phone}
    return render(request, "lab3/filled-contacts.html", context=data)


def about_project(request):
    return render(request, 'lab3/about-project.html')


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
    data = {"members":(Tima, Daurbek)}
    return render(request, 'lab3/about-members.html', context=data)


def member_contacts(request):
    Tima = {"phone": "+7 707 619 28 78",
            "email": "temirlan.muslimov.1@gmail.com",
            "address": "Aksay-2"}
    Daurbek = {"phone": "+7 778 911 58 35",
               "email": "example@gmail.com",
               "address": "Varlamova"}
    data = {"members": (Tima, Daurbek)}
    return render(request, 'lab3/member-contacts.html', context=data)
