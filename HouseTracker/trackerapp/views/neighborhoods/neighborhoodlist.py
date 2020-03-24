import sqlite3
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, reverse, redirect
from trackerapp.models.neighborhood import Neighborhood
from ..connection import Connection




def neighborhood_list(request):
    if request.method == 'GET':
        neighborhoods = Neighborhood.objects.all()
        template = 'neighborhoods/list.html'
        context = {
            'neighborhoods': neighborhoods
        }
        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST
        new_neighborhood = Neighborhood(
             name = form_data['name'],
        )
        return redirect(reverse('trackerapp:neighborhood_list'))
                

