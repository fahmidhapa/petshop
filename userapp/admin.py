from django.contrib import admin
from . models import Reg_tbl,pet_tbl,cart_tbl

# Register your models here.


admin.site.register(Reg_tbl)
admin.site.register(pet_tbl)
admin.site.register(cart_tbl)