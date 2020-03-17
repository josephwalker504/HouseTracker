import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def getNeighborhoods():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Library)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            n.id,
            n.name,
        from trackerapp_neighbor 
        """)

        return db_cursor.fetchall()