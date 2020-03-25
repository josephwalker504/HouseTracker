import sqlite3
from django.shortcuts import render, redirect, reverse
from trackerapp.models import House, Neighborhood
from ..connection import Connection
 

def houselist(request):
    if request.method == 'GET':
        allHouses = House.objects.all()
        template = 'houses/houselist.html'
        context = {
                'allHouses': allHouses
            }

        return render(request, template, context)
               
    elif request.method == 'POST':
            form_data = request.POST
            newHouse = House.objects.create(
                address = form_data['address'],
                # image = form_data['image'],
                askingPrice = form_data['askingPrice'],
                sellingPrice = form_data['sellingPrice'],
                notes = form_data['notes'],
    
            )
            
    newHouse.save()


    return redirect(reverse('trackerapp:houses'))


