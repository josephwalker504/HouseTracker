import sqlite3
from django.shortcuts import render
from trackerapp.models import House
from ..connection import Connection


def houselist(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT 
                address, 
                sellingPrice, 
                askingPrice,
                image,
                notes,
                investorId_id,
                userId_id
            FROM trackerapp_house h;
            """)

            allHouses = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                house = House()
                # house.id = row['id']
                house.address = row['address']
                house.image = row['image']
                house.askingPrice = row['askingPrice']
                house.sellingPrice = row['sellingPrice']
                house.notes = row['notes']
                house.investorId_id = row['investorId_id']
                house.userId_id = row['userId_id']

                allHouses.append(house)

        template = 'houses/houselist.html'
        context = {
            'allHouses': allHouses
        }

        return render(request, template, context)