from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
	path('', views.home, name='home'),
	path('nasa', views.nasa, name='nasa'),
	path('noaa', views.noaa, name='noaa'),
	path('dataRequest', views.dataRequest, name='dataRequest'),
	path('viewNOAA', views.viewNOAA, name='viewNOAA'),
	path('viewNASA', views.viewNASA, name='viewNASA'),
	path('logout', views.logout, name='logout')
]