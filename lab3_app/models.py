from django.db import models


# Create your models here.
class Colors(models.Model):
    name = models.TextField(max_length=50)


class Materials(models.Model):
    name = models.TextField(max_length=50)


class Users(models.Model):
    name = models.TextField(max_length=20)
    surname = models.TextField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.TextField(max_length=20)
    phone = models.TextField(max_length=20)


class Shoes(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=1000)
    for_man = models.BooleanField(default=True)
    for_child = models.BooleanField(default=True)
    image = models.ImageField(upload_to="images/")
    country = models.TextField(max_length=50)
    company = models.TextField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    is_purchasable = models.BooleanField(default=False)


class Shoes_count(models.Model):
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    size = models.TextField()
    count = models.PositiveIntegerField(default=0)


class Shoes_material(models.Model):
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE)


class Shoes_colors(models.Model):
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)


class Carts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoes, on_delete=models.CASCADE)
    size = models.TextField()
    count = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
