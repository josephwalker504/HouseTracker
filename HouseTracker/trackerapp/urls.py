from django.urls import include, path
from django.conf.urls import url
from .views import *

app_name = "trackerapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^houses$', houselist, name='houses'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logoutUser, name='logout'),

]