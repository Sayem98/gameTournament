from django.shortcuts import render
from django.views import View
from .forms import LoginForm, RegisterForm
from .models import UserModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'login-site/register.html', {
            'form': form,
            'pass_not_match': False
        })

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if request.POST['password'] != request.POST['confirm_password']:
            return render(request, 'login-site/register.html', {
                'form': form,
                'pass_not_match': True
            })
        else:

            if form.is_valid():
                    user = UserModel(your_name=request.POST['your_name'], email=request.POST['email'],
                                     password=request.POST['password'], user_image=request.FILES['user_image'],
                                     pubgID=request.POST['pubgID'], Sea_of_theves_id=request.POST['Sea_of_theves_id'],
                                     Call_of_duty_id=request.POST['Call_of_duty_id'], phone=request.POST['phone'])

                    user.save()
                    return redirect('login')
            return render(request, 'login-site/register.html', {
                'form': form,
                'pass_not_match': False
            })


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login-site/login.html', {
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                user = UserModel.objects.get(email=request.POST['email'])

            except:
                user = None

            # print(user)
            if user is None:
                return render(request, 'login-site/login.html', {
                    'form': form,
                    'in_valid_mail': True,
                    'in_valid_password': False
                })
            else:
                print(user.password)
                print(request.POST['password'])
                if user.password != request.POST['password']:
                    return render(request, 'login-site/login.html', {
                        'form': form,
                        'in_valid_mail': False,
                        'in_valid_password': True
                    })
            return redirect('home', user.id)
        return render(request, 'login-site/login.html', {
            'form': form
        })
