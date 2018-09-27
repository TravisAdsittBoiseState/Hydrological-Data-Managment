from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.template import Context, loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.conf import settings
from .forms import DataRequestForm
import os

def home(request):
	user = request.user
	return render(request, 'core/home.html')

@login_required
def logout(request):
	django_logout(request) # logout the user
	return redirect(home)

@login_required
def nasa(request):
	user = request.user
	path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
	myfiles = os.path.join(path, 'downloaded-files/n5eil01u.ecs.nsidc.org')
	file_list = os.listdir(myfiles)
	num_files = count(myfiles)
	return render_to_response('core/files.tpl.html', {'organization': 'NASA', 'user': user, 'files': file_list, 'num_files': num_files})

@login_required
def noaa(request):
	user = request.user
	path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
	myfiles = os.path.join(path, 'downloaded-files/ftp.ssec.wisc.edu')
	file_list = os.listdir(myfiles)
	num_files = count(myfiles)
	return render_to_response('core/files.tpl.html', {'organization': 'NOAA', 'user': user, 'files': file_list, 'num_files': num_files})

@login_required
def dataRequest(request):
    if request.method == "POST":
        form = DataRequestForm(request.POST)
        if form.is_valid():
            dr = form.save(commit=False)
            dr.save()
            return redirect(home)
    else:
        form = DataRequestForm()
    return render(request, 'core/dataRequest.html', {'form': form})

#-- Helper Functions --#

# returns # of files in dir and subdirs
def count(dir, counter=0):
    for pack in os.walk(dir):
        for f in pack[2]:
            counter += 1
    return str(counter)