from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

# Custom UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'dgfi_id')  # Add more fields if needed

    # Apply Bootstrap form-control to all fields
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    dgfi_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# Custom UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'dgfi_id', 'is_active', 'is_admin')  # Add more fields if needed

    # Apply Bootstrap form-control to all fields
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    dgfi_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    is_admin = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
