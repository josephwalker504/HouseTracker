from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from trackerapp.models import Neighborhood

def get_neighborhood(neighborhood_id):
    return Neighborhood.objects.get(pk=neighborhood_id)



@login_required
def neighborhood_detail(request, neighborhood_id):
    
    if request.method == 'GET':
        neighborhood = get_neighborhood(neighborhood_id)
        template = 'neighborhoods/detail.html'
        return render(request, template, {'neighborhood': neighborhood})
        

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == 'DELETE'
        ):
            neighborhood = Neighborhood.objects.get(id=neighborhood_id)
            neighborhood.delete()
            
            return redirect(reverse('trackerapp:neighborhoods'))

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == 'PUT'
        ):

            neighborhood_to_update = Neighborhood.objects.get(id=neighborhood_id)
            
            neighborhood_to_update.name = form_data['name']            
            neighborhood_to_update.save()
            
            return redirect(reverse('trackerapp:neighborhood_list'))