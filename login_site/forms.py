from django import forms


class RegisterForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=20)
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    user_image = forms.ImageField(label='My Photo')
    pubgID = forms.CharField(label='PUBG id', max_length=10, widget=forms.NumberInput, required=False)
    Sea_of_theves_id = forms.CharField(label='Sea of theves id',  max_length=10, widget=forms.NumberInput, required=False)
    Call_of_duty_id = forms.CharField(label='Call od duty id', max_length=10, widget=forms.NumberInput, required=False)
    phone = forms.CharField(label='Phone No', widget=forms.NumberInput(attrs={
        'minlength': 8,
        'maxlength': 10
    }))


class LoginForm(forms.Form):
    email = forms.EmailField(label='Your email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
