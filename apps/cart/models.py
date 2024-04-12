from django.db import models

from apps.menu.models import Menu
from apps.user.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Menu)


