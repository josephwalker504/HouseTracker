import sqlite3
from django.shortcuts import render, redirect, reverse
from trackerapp.models import House
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

    newHouse = House(
            address = form_data['address'],
            image = form_data['image'],
            askingPrice = form_data['askingPrice'],
            sellingPrice = form_data['sellingPrice'],
            notes = form_data['notes'],
            investorId_id = form_data['investorId_id'],
            userId_id = form_data['userId_id']
            )
            
    newHouse.save()

    return redirect(reverse('trackerapp: houses/houseslist'))


