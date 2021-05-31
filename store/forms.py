from django import forms
from django.forms import fields, widgets
from .models import Category, Product

class NewCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

  

class NewProduct(forms.ModelForm):

    class Meta:
        model = Product
        fields =( 'category', 'title','description','selling', 'price', 'image',)
     