from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.text_box, name='text_box'),

]

