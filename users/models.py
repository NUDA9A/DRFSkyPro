from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import AUTH_USER_MODEL
from courses.models import Lesson, Course

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="телефон", **NULLABLE)
    city = models.CharField(max_length=150, verbose_name="город", **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name="аватарка", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    date = models.DateField(auto_now_add=True, verbose_name="Дата оплаты")
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, verbose_name="Оплаченный урок", **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name="Оплаченный курс", **NULLABLE)
    price = models.PositiveIntegerField(verbose_name="Стоимость")
    method_choices = {"Наличными": "cash", "Перевод": "card"}
    payment_method = models.CharField(max_length=10, choices=method_choices, default="card", verbose_name="Способо оплаты")

    def __str__(self):
        return f'{self.payment_method} {self.course}'

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
