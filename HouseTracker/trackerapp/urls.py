from django.urls import include, path
from django.conf.urls import url
from .views import *

app_name = "trackerapp"

urlpatterns = [
    path('', home, name='home'),
    path('houses/', houselist, name='houses'),
    path('houses/<int:house_id>/', house_detail, name='house_detail'),
    path('houseform', house_form, name='house_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logoutUser, name='logout'),
    path('houses/<int:house_id>/', house_edit_form, name='house_edit_form'),
    path('neighborhoodform', neighborhood_form, name='neighborhood_form'),

]