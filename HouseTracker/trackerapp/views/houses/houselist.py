import sqlite3
from django.shortcuts import render, redirect, reverse
from trackerapp.models import House, Neighborhood
from ..connection import Connection
 

def houselist(request):
    if request.method == 'GET':
        current_neighborhood = Neighborhood.objects.filter(user_id = request.user.id)
        allHouses = House.objects.filter(userId_id = request.user.id )
        template = 'houses/houselist.html'
        context = {
                'allHouses': allHouses
            }

        return render(request, template, context)
               
    elif request.method == 'POST':
            form_data = request.POST
            newHouse = House.objects.create(
                userId_id = request.user.id,
                address = form_data['address'],
                image = form_data['image'],
                askingPrice = form_data['askingPrice'],
                sellingPrice = form_data['sellingPrice'],
                notes = form_data['notes'],
    
            )
            
    newHouse.save()


    return redirect(reverse('trackerapp:houses'))


