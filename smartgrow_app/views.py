# smartgrow_app/views.py
from django.shortcuts import render
from .models import Crop

def home(request):
    crops = Crop.objects.all()
    return render(request, 'home.html', {'crops': crops})