from django.db import models

from apps.branch.models import Branch


class Category(models.Model):
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f'{self.name}, {self.id}'


class Menu(models.Model):
    branch = models.ManyToManyField(Branch, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="static/images/menu/", null=True, blank=True)

    def __str__(self):
        return self.title


class Weight(models.Model):
    weight = models.FloatField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.weight}g - ${self.price}"
