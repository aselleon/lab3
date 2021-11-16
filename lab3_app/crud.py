from lab3_app.models import *
from lab3_app.classes import *


def get_all_shoes():
    return Shoes.objects.all()


def get_all_men_shoes():
    shoes = Shoes.objects.filter(for_man=True)
    return_shoes = []
    for shoe in shoes:
        sizes = get_shoe_count(shoe.id)
        temp_shoe = Shoe(shoe.name, shoe.price, sizes, shoe.image.url)
        return_shoes.append(temp_shoe)
    return return_shoes


def get_all_women_shoes():
    shoes = Shoes.objects.filter(for_man=False)
    return_shoes = []
    for shoe in shoes:
        sizes = get_shoe_count(shoe.id)
        temp_shoe = Shoe(shoe.name, shoe.price, sizes, shoe.image.url)
        return_shoes.append(temp_shoe)
    return return_shoes


def get_all_colors():
    return Colors.objects.all()


def get_all_materials():
    return Materials.objects.all()


def get_all_users():
    return Users.objects.all()


def get_all_shoes_count():
    return Shoes_count.objects.all()


def get_all_shoes_material():
    return Shoes_material.objects.all()


def get_all_carts():
    return Carts.objects.all()


def get_shoe_material(id):
    return Shoes_material.objects.filter(shoe=id)


def get_shoe_color(id):
    return Shoes_colors.objects.filter(shoe=id)


def get_shoe_count(id):
    return Shoes_count.objects.filter(shoe=id)
