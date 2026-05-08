from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product
        fields = ['name', 'category', 'price', 'quantity', 'color', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Product Name',
                'class': 'form-control'
            }),
            'category': forms.TextInput(attrs={
                'placeholder': 'Category',
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Price',
                'class': 'form-control'
            }),
            'quantity': forms.NumberInput(attrs={
                'placeholder': 'Quantity',
                'class': 'form-control'
            }),
            'color': forms.TextInput(attrs={
                'placeholder': 'Color',
                'class': 'form-control'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError('Invalid field')
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError('Invalid field')
        return price

    def clean_quantity(self):
        qty = self.cleaned_data.get('quantity')
        if qty is not None and qty < 1:
            raise forms.ValidationError('Invalid field')
        return qty