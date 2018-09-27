"""geominerSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from django.conf.urls import include, url
from django.contrib.auth.views import LoginView
from core import views as core_views

urlpatterns = [
	#path('', include('core.urls')),
	url(r'', include('core.urls', namespace='home')),
    url(r'^admin/', admin.site.urls),
	url(r'^$', core_views.home, name='home'),
    url(r'^$', core_views.nasa, name='nasa'),
    url(r'^$', core_views.noaa, name='noaa'),
	url(r'^$', core_views.dataRequest, name='dataRequest'),
    url(r'^login/$', LoginView.as_view()),
    url(r'^logout/', include('core.urls', namespace='logout')),
    url("^soc/", include("social_django.urls", namespace="social")),
    url(r'^', include('core.urls', namespace='nasa')),
    url(r'^', include('core.urls', namespace='noaa')),
	url(r'^', include('core.urls', namespace='dataRequest')),
	
	#path('', RedirectView.as_view(url=r'^login/', permanent=True))
]
