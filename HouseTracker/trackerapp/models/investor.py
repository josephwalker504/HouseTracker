from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User





class Investor (models.Model):
    userId = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    lookingFor = models.CharField(max_length=300)
    budget = models.IntegerField(max_length=None)
    

    class Meta:
        verbose_name = ("investor")
        verbose_name_plural = ("investors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("investordetail", kwargs={"pk": self.pk})
