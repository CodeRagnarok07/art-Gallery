from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),

    #crud
    path('new_category/', new_category, name="new_category"),
    path('Add_article/', Add_article, name="Add_article"),




    path('<slug:category>/<slug:slug>/', product_detail, name="detail"),
    path('<slug:slug>/', view_category, name="view_category"),


    
]
