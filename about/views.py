from django.shortcuts import render

from .models import About
def abt(request):
    abouts = About.objects
    return render(request, 'about/abt.html', {'abouts':abouts})
