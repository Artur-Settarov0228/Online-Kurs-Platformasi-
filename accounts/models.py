from django.contrib.auth.models import AbstractUser
from django.db import models


class Foydalanuvchi(AbstractUser):
    ROLLAR = (
        ('oquvchi', 'Oʻquvchi'),
        ('oqituvchi', 'Oʻqituvchi'),
    )

    rol = models.CharField(max_length=20 , choices=ROLLAR, default='oquvchi', verbose_name="Rol")
    telifon = models.CharField(max_length= 20, blank=True, verbose_name="Telifon raqam")
    bio = models.TextField(max_length=300, blank=True, verbose_name="Biografiya")
    avatar = models.ImageField(upload_to='avatarlar/', blank=True, null=True, verbose_name="Profil rasmi")
    
    yaratilgan_sana = models.DateTimeField(auto_now_add=True, verbose_name= "Yartilgan sana")

    class Meta:
        verbose_name = "Foydalanuchi"
        verbose_name_plual = "Foydalanuvchilar"

    def __str__(self):
        return self.username