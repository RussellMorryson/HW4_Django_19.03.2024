from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=400)
    price = forms.FloatField(min_value=0)    
    image = forms.ImageField()