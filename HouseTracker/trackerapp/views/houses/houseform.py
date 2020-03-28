import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from trackerapp.models import House
from trackerapp.models import Neighborhood
from trackerapp.models import model_factory
from ..connection import Connection




def get_neighborhood():

    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Neighborhood)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     select
    #         n.id,
    #         n.name
    #     from trackerapp_neighborhood n 
    #     """)

    #     return db_cursor.fetchall()
    all_neighborhood = Neighborhood.objects.all()

    return all_neighborhood

def get_house(house_id):
    all_houses = House.objects.get(pk=house_id)
    return all_houses



def house_form(request,):
    if request.method == 'GET':
        # house = get_house()
        neighborhoods = Neighborhood.objects.filter(user_id = request.user.id) 
        template = 'houses/houseform.html'
        context = {
            'all_neighborhoods': neighborhoods
        }

        return render(request, template, context)



def house_edit_form(request, house_id):
    if request.method == 'GET':
        house = get_house(house_id)
        neighborhoods = Neighborhood.objects.filter(user_id = request.user.id)
        template = 'houses/houseform.html'
        context = {
            'house': house,
            'all_neighborhoods': neighborhoods
        }
        return render(request, template, context)
        
    # else: return render(request, 'houses/houselist.html' )