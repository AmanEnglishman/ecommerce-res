from django.db import models


class Booth(models.Model):
    title = models.CharField(max_length=100)
    capacity = models.IntegerField()
    free = models.BooleanField()

    def __str__(self):
        return self.title


class Branch(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    booths = models.ManyToManyField(Booth, null=True, blank=True)

    def __str__(self):
        return self.title


class BranchNumber(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    number = models.CharField(max_length=100)

    def __str__(self):
        return self.number


class BranchImages(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/branch/')

    def __str__(self):
        return self.image.name


class BoothImages(models.Model):
    booth = models.ForeignKey(Booth, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images/booth/')

    def __str__(self):
        return self.image.name
