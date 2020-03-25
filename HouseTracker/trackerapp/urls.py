from django.urls import include, path
from django.conf.urls import url
from .views import *

app_name = "trackerapp"

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name="register"),
    path('logout/', logoutUser, name='logout'),
    path('houseform', house_form, name='house_form'),
    path('houses/', houselist, name='houses'),
    path('houses/<int:house_id>/', house_detail, name='house_detail'),
    path('houses/<int:house_id>/form', house_edit_form, name='house_edit_form'),
    path('neighborhoodform', neighborhood_form, name='neighborhood_form'),
    path('neighborhoods/', neighborhood_list, name='neighborhood_list'),
    path('neighborhood/<int:neighborhood_id>/', neighborhood_detail, name='neighborhood_detail'),
    path('neighborhood/<int:neighborhood_id>/form', neighborhood_edit_form, name='neighborhood_edit_form'),
]