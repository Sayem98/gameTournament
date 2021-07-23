from django.shortcuts import render
from django.views import View
from login_site.models import UserModel
from tournaments.models import TournamentsModel
from django.shortcuts import redirect


# Create your views here.


class ProfileView(View):
    def get(self, request, id):
        try:
            user = UserModel.objects.get(id=id)
            request.session['user_id'] = user.id



        except:
            user = None
        all_tournaments = TournamentsModel.objects.filter(your_email=user.email)

        catagories = ['PUBG', 'Call of Duty', 'Sea of Thieves']
        return render(request, 'profile_site/profile.html', {
            'user': user,
            'catagories': catagories,
            'all_tournaments': all_tournaments
        })


class HomeView(View):
    def get(self, request):
        id = request.session['user_id']
        return redirect('home', id=id)


class UpdateAccountView(View):
    def get(self, request):
        id = request.session['user_id']

        return render(request, 'profile_site/my_account.html', {
            'user': UserModel.objects.get(id=id)
        })

    def post(self, request):
        pass
