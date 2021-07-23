from django.shortcuts import render
from django.views import View
from .forms import TournamentsForm, TournamentRegisterForm
from .models import TournamentsModel, TeamsModel
from django.shortcuts import redirect
from django.http import HttpResponse
from login_site.models import UserModel
# Create your views here.


class TournamentsView(View):
    def get(self, request):
        form = TournamentsForm()
        return render(request, 'tournaments/tournaments.html', {
            'form': form
        })

    def post(self, request):
        form = TournamentsForm(request.POST)
        id = request.session['user_id']
        if form.is_valid():
            tournament = TournamentsModel(game_type=form.cleaned_data['game_type'],
                                          tournament_name=form.cleaned_data['tournament_name'],
                                          your_email=form.cleaned_data['your_email'], fee=form.cleaned_data['fee'],
                                          team_numbers=form.cleaned_data['team_numbers'], creator_name=UserModel.objects.filter(id=id)[0])
            tournament.save()

            return redirect('home', id=id)  # to home but session is needed...But what if multiple people are trying?


class All_TournamentsView(View):
    def get(self, request):
        all_tournaments = TournamentsModel.objects.all()

        return render(request, 'tournaments/all_tournamments.html', {
            'all_tournaments': all_tournaments
        })


class A_tournamentView(View):
    def get(self, request, id):
        try:
            tournament = TournamentsModel.objects.get(id=id)
            registered_teams = tournament.teams.all()

        except:
            tournament = None
        return render(request, 'tournaments/a_tournament.html', {
            'tournament': tournament,
            'creator': tournament.creator_name,
            'teams': registered_teams,
            'slots': int(tournament.team_numbers) - registered_teams.count()
        })

    def post(self, request):
        pass


class RegisterTournamentView(View):
    def get(self, request, id):
        tournament = TournamentsModel.objects.get(id=id)
        request.session['tournament_id'] = tournament.id
        form = TournamentRegisterForm()
        return render(request, 'tournaments/register_a_tournament.html', {
            'form': form,
            'id': tournament.id,
            'registered_teams': tournament.teams.all()
        })

    def post(self, request, id):
        team = TournamentRegisterForm(request.POST)
        # tournament = request.session['tournament_id']
        if team.is_valid():

            team_model = TeamsModel(team_name=team.cleaned_data['team_name'], player1=team.cleaned_data['player1'], player2=team.cleaned_data['player2'],
                                    player3=team.cleaned_data['player3'], player4=team.cleaned_data['player4'],
                                    leader=team.cleaned_data['leader'], tournament=TournamentsModel.objects.filter(id=id)[0])

            team_model.save()
            return redirect('a-tournament', id)
        return render(request, 'tournaments/register_a_tournament.html', {
            'form': team,
            'id': id
        })