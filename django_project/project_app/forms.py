from .models import *
from django.forms import ModelForm,TextInput,NumberInput,FileInput,DateTimeInput,PasswordInput
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class RegisterForm(ModelForm):
    phone_number = PhoneNumberField(
        widget = PhoneNumberPrefixWidget(initial='KZ')
    )
    class Meta:
        model=Registration
        fields= '__all__'
        widgets = {
            'date_of_birth': DateTimeInput(attrs={'type':'date'}),
            'password':PasswordInput(attrs={'placeholder': 'please enter password'}),
            }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and Registration.objects.filter(username=username).exists():
            raise forms.ValidationError('This username has already been taken!')
        return username
