from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")

        return cleaned_data


class LostItemForm(forms.Form):
    item_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.CharField(max_length=50)
    lost_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)


class FoundItemForm(forms.Form):
    item_name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.CharField(max_length=50)
    found_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    location = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)


class ClaimRequestForm(forms.Form):
    proof_details = forms.CharField(widget=forms.Textarea)