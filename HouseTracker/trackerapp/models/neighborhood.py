from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Neighborhood (models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = ("neighborhood")
        verbose_name_plural = ("neighborhoods")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("neighborhood_detail", kwargs={"pk": self.pk})
