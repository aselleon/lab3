from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Shoes)
admin.site.register(Shoes_count)