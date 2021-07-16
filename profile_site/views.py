from django.shortcuts import render
from django.views import View
from login_site.models import UserModel

# Create your views here.


class ProfileView(View):
    def get(self, request, id):
        try:
            user = UserModel.objects.get(id=id)

        except:
            user = None
        catagories = ['PUBG', 'Call of Duty', 'Sea of Thieves' ]
        return render(request, 'profile_site/profile.html', {
            'user': user,
            'catagories': catagories
        })
