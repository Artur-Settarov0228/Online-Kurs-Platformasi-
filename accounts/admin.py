from django.contrib import admin

from . models import Foydalanuvchi

# Register your models here.
@admin.register(Foydalanuvchi)
class FoydalanuvchiAdmin(admin.ModelAdmin):

    list_display = ['username', 'email', 'rol', 'is_staff', 'Yartilgan_sana']

    list_filter = ['rol', 'is_staff', 'is_superuser']

    search_fields = ['username', 'email', 'telefon']
        # Sahifadagi elementlar soni 
    list_per_page = 20

