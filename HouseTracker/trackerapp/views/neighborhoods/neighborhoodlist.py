import sqlite3
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, reverse, redirect
from trackerapp.models.neighborhood import Neighborhood





def neighborhood_list(request):
    if request.method == 'GET':
        neighborhoods = Neighborhood.objects.filter(user_id = request.user.id)
        template = 'neighborhoods/list.html'
        context = {
            'neighborhoods': neighborhoods
        }
        return render(request, template, context)
    elif request.method == 'POST':
        form_data = request.POST
        new_neighborhood = Neighborhood(
             name = form_data['name'],
              user_id = request.user.id
        )
        new_neighborhood.save()
        return redirect(reverse('trackerapp:neighborhood_list'))
                

