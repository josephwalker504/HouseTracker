import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from trackerapp.models import House
from trackerapp.models import Neighborhood
from trackerapp.models import model_factory
from ..connection import Connection
from .housedetails import getHouse


def get_neighborhoods():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Neighborhood)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            n.id,
            n.name
        from trackerapp_neighborhood n 
        """)

        return db_cursor.fetchall()


def house_form(request):
    if request.method == 'GET':
        neighborhoods = get_neighborhoods()
        template = 'houses/houseform.html'
        context = {
            'allNeighborhoods': neighborhoods
        }

        return render(request, template, context)


def house_edit_form(request, house_id):

    if request.method == 'GET':
        house = getHouse(house_id)
        neighborhoods = get_neighborhoods()

        template = 'houses/houseform.html'
        context = {
            'house': house,
            'all_neighborhood': neighborhoods
        }

        return render(request, template, context)