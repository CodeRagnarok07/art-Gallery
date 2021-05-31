from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
# Create your views here.

from django.contrib.auth.decorators import login_required

def index(request):
    products = Product.objects.all().order_by('-date_add')

    ctx = {
        'products': products
    }
    return render(request, 'store/index.html', ctx)


def product_detail(request, category, slug):
    product = get_object_or_404(Product, slug = slug)

    ctx = {
        'product': product
    }
    return render(request, 'store/detail.html', ctx)

def view_category(request, slug):
    category = get_object_or_404(Category, slug = slug)
    products = category.products.all()

    ctx = {
        'category': category,
        'products': products
    }

    return render(request, 'store/category.html', ctx)


from .forms import NewCategory, NewProduct
from django.utils.text import slugify


@login_required
def new_category(request):
    if request.method == 'POST':      
        form = NewCategory(request.POST)  


        #crea una nueva categoria con una url bien echa automaticamente
        if form.is_valid():   
            category = form.save(commit=False)
            category.slug = slugify(category.name)             
            form.save()              
            return redirect('index')
    else:                        
        form = NewCategory()


    ctx = {
        'form': form
    }
    return render(request, 'store/new_category.html', ctx)


@login_required
def Add_article(request):
    if request.method == 'POST':      
        form = NewProduct(request.POST)  
        #crea una nueva categoria con una url bien echa automaticamente
        if form.is_valid():   
            product = form.save(commit=False)
            product.slug = slugify(product.name)             
            form.save()              
            return redirect('index')
    else:                        
        form = NewProduct()


    ctx = {
        'form': form
    }
    return render(request, 'store/CRUD.html', ctx)