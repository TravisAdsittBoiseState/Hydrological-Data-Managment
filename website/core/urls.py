from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
	path('', views.home, name='home'),
	path('nasa', views.nasa, name='nasa'),
	path('noaa', views.noaa, name='noaa'),
	path('name', views.get_name, name='get_name'),
	path('logout', views.logout, name='logout')
]