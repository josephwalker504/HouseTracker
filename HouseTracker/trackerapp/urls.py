from django.urls import include, path
from .views import *

app_name = "trackerapp"

urlpatterns = [
    path('home', home, name='home'),
    path('houses/', houselist, name='houses'),
    path('accounts/', include('django.contrib.auth.urls')),

]