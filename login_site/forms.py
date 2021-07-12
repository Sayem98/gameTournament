from django import forms


class RegisterForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=10, widget=forms.PasswordInput)


class LoginForm(forms.Form):
    email = forms.EmailField(label='Your email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

