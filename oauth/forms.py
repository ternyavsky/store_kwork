
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField, PasswordResetForm, SetPasswordForm
from .models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "text",
        'id': "username",
        'placeholder':"Имя пользователя",
        'name':'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "current-password",
        'class':'form-control',
        'type': "password",
        'placeholder':"Пароль",
        'name':'password'}),
    ) 


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        
        max_length=254,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            'class':'form-control',
            'id':'email',
            'placeholder':'Email',
            'name':'email',
            'type':'email'})
    )

class ConfirmPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
       
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
            'class':'form-control',
            'id':'password',
            'placeholder':'Пароль',
            'name':'password',
            'type':'password'})
       
    )
    new_password2 = forms.CharField(
      
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
        'class':'form-control',
            'id':'password',
            'placeholder':'Повторите пароль',
            'name':'password',
            'type':'password'}))
    
class ChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['photo','username','email','first_name','last_name']
        widgets = {
            'photo': forms.FileInput(attrs={
                'name':'photo'
            }
            ),
                'username': forms.TextInput(attrs={
                        'class':"form-control",
                        'type':"text",
                        'name':'username',
                        'id':'fullName'}),
                'email': forms.EmailInput(attrs={
                        'class':"form-control",
                        'type':"email",
                        'name':'email',
                        'id':'eMail'}),
                'first_name': forms.TextInput(attrs={
                        'class':"form-control",
                        'type':"text",
                        'name':'first_name',
                        'id':'Street'
                        }),
                'last_name': forms.TextInput(attrs={
                        'class':"form-control",
                        'type':"text",
                        'name':'last_name',
                        'id':'ciTy'
                }),
                
                
        }

class RegistrationForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "username",
        'placeholder':"Имя пользователя",
        'name':'username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "autofocus": True,
        'class':'form-control',
        'type': "email",
        'id': "floatingInput",
        'placeholder':"E-mail",
        'name':'email'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "new-password",
        'class':'form-control',
        'type': "password",
        'id': "password",
        'placeholder':"Пароль",
        'name':'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "autocomplete": "new-password",
        'class':'form-control',
        'type': "password",
        'id': "password",
        'placeholder':"Повторите пароль",
        'name':'password2'
    }))

    class Meta:
        model = User
        fields = ('username', 'email' )