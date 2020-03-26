import sqlite3
from django.shortcuts import render, redirect, reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from trackerapp.models import model_factory
from ..connection import Connection
from trackerapp.models import Neighborhood





def get_neighborhoods(neighborhood_id):
    return Neighborhood.objects.get(pk=neighborhood_id)



@login_required
def neighborhood_form(request):
    if request.method == 'GET':
        neighborhoods = Neighborhood.objects.all()
        template = 'neighborhoods/form.html'
        
        return render(request, template,)

@login_required
def neighborhood_edit_form(request, neighborhood_id):

    if request.method == 'GET':
        neighborhood = get_neighborhoods(neighborhood_id)
        template = 'neighborhoods/form.html'
        context = {
            'neighborhood': neighborhood,
        }
        return render(request, template, context)

