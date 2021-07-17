from django.shortcuts import render
from django.views import View
from .forms import TournamentsForm
from .models import TournamentsModel
from django.shortcuts import redirect
# Create your views here.


class TournamentsView(View):
    def get(self, request):
        form = TournamentsForm()
        return render(request, 'tournaments/tournaments.html', {
            'form': form
        })

    def post(self, request):
        form = TournamentsForm(request.POST)
        if form.is_valid():
            tournament = TournamentsModel(game_type=form.cleaned_data['game_type'], tournament_name=form.cleaned_data['tournament_name'], your_email=form.cleaned_data['your_email'], fee=form.cleaned_data['fee'], team_numbers=form.cleaned_data['team_numbers'])
            tournament.save()
            id = request.session['user_id']
            return redirect('home', id=id) # to home but session is needed...But what if multiple people are trying?