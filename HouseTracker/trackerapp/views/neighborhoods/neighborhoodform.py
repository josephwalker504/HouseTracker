import sqlite3
from django.shortcuts import render, redirect, reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from trackerapp.models import model_factory
from ..connection import Connection
from trackerapp.models import Neighborhood





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


@login_required
def neighborhood_form(request):
    if request.method == 'GET':
        neighborhoods = get_neighborhoods()
        template = 'neighborhoods/form.html'
        context = {
            'neighborhoods': neighborhoods
        }
        return render(request, template, context)

@login_required
def neighborhood_edit_form(request, neighborhood_id):

    if request.method == 'GET':
        neighborhood = get_neighborhoods(neighborhood_id)
        template = 'neighborhoods/form.html'
        context = {
            'neighborhood': neighborhood,
        }
        return render(request, template, context)

