from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout

def logoutUser(request):
    logout(request)
    return redirect(reverse('trackerapp:home'))