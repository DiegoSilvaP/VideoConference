from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    is_medical = forms.BooleanField(required=False)
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_medical']

        labels = {
            'username':'Nombre de usuario',
            'first_name':'Nombre',
            'last_name':'Apellido',
            'email': 'Correo',
            'password1':'Pass',
            'password2':'Confirmacion',
            'is_medical':'Es medico',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class' : 'form-control'}),
            'first_name':forms.TextInput(attrs={'class' : 'form-control'}),
            'last_name':forms.TextInput(attrs={'class' : 'form-control'}),
            'email': forms.EmailInput(attrs={'class' : 'form-control'}),
            'password1':forms.PasswordInput(attrs={'class' : 'form-control'}),
            'password2':forms.PasswordInput(attrs={'class' : 'form-control'}),
            'is_medical':forms.CheckboxInput(attrs={'class' : 'form-control'}),
        }


# class LoginForm(AuthenticationForm):
#     # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     is_medical = forms.BooleanField(required=False, help_text='Optional.')
#     # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('is_medical',)

#         widgets = {
            
#             'is_medical':forms.CheckboxSelectMultiple(),
#         }