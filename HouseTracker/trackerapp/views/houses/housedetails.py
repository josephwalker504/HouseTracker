import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from trackerapp.models import House


def getHouse(houseid):

     return House.objects.get(pk=houseid)


def housedetails(request, houseid):
    if request.method == 'GET':
        house = getHouse(houseid)
        template_name = 'houses/housedetail.html'
        return render(request, template_name, {'house': house})

    elif request.method == 'POST':
        form_data = request.POST

  # Check if this POST is for editing a house
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
         # retrieve it first
            houseToUpdate = House.objects.get(pk=houseid)
        # Reassign a property's value
            houseToUpdate.address = form_data['address']
            houseToUpdate.image = form_data['image']
            houseToUpdate.askingPrice = form_data['askingPrice']
            houseToUpdate.sellingPrice = form_data['sellingPrice']
            houseToUpdate.notes = form_data['notes']
            houseToUpdate.investorId_id = form_data['investorId_id']
            houseToUpdate.userId_id = form_data['userId_id']


            houseToUpdate.save()

            return redirect(reverse('trackerapp:houses'))