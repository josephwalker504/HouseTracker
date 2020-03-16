from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .investor import Investor



class House (models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    investorId = models.ForeignKey(Investor, on_delete=models.CASCADE)
    image = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    askingPrice = models.IntegerField(max_length=None)
    sellingPrice = models.IntegerField(max_length=None)
    notes = models.CharField(max_length=300)

    

    class Meta:
        verbose_name = ("House")
        verbose_name_plural = ("Houses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("House_detail", kwargs={"pk": self.pk})
