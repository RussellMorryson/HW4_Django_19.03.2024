from django.shortcuts import render

# Create your views here.
import logging
from .forms import UserForm, ProductForm
from .models import User, Product
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)
def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp/user_form.html', {'form': form})

def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            logger.info(f'Получили {name=}, {description=}, {price=}, {image=}.')
            
            fs = FileSystemStorage()
            fs.save(image.name, image)

            product = Product(name=name, description=description, price=price, image=image.name)
            product.save()
    else:
        form = ProductForm()
    return render(request, 'myapp/product_form.html', {'form': form})
