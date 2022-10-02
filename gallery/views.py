from ctypes.wintypes import PHKEY
from django.shortcuts import render, get_object_or_404
from .models import Gallery
def gall(request):
    gals = Gallery.objects
    return render(request, 'gallery/gall.html', {'gals':gals})