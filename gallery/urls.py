from django.urls import path
from .import views
urlpatterns = [
    path('',views.gall, name='gall'),]