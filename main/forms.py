from django import forms
from .models import Contacts

class ContactForm(forms.ModelForm):
    TARIFF_CHOICES = [
        ('basic', 'Базовый — 29 900 тг/месяц'),
        ('advanced', 'Продвинутый — 49 900 тг/месяц'),
        ('premium', 'Премиум — 79 900 тг/месяц'),
    ]

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя *'}), required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваш город *'}), required=True)
    tariff = forms.ChoiceField(choices=TARIFF_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Ваш тарифный план *'}), required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ваше Email *'}), required=True)
    number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон *'}), max_length=50, required=True)

    class Meta:
        model = Contacts
        fields = ('name', 'city', 'email', 'number', 'tariff')
