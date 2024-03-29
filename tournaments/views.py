from django.shortcuts import render
from django.views import View
from .forms import TournamentsForm, TournamentRegisterForm, UpdateTournamentsForm
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
                                          team_numbers=form.cleaned_data['team_numbers'],
                                          creator_name=UserModel.objects.filter(id=id)[0],
                                          last_register_date=form.cleaned_data['last_register_date'])
            tournament.save()

            return redirect('home', id=id)  # to home but session is needed...But what if multiple people are trying?
        return render(request, 'tournaments/tournaments.html', {
            'form': form
        })


class All_TournamentsView(View):
    def get(self, request):
        all_tournaments = TournamentsModel.objects.all()

        return render(request, 'tournaments/all_tournamments.html', {
            'all_tournaments': all_tournaments
        })


class A_tournamentView(View):
    def get(self, request, slug):
        print(slug)
        try:
            tournament = TournamentsModel.objects.get(slug=slug)
            registered_teams = tournament.teams.all()

        except:
            tournament = None
        if tournament.creator_name.id == request.session['user_id']:
            is_creator = True
            # request.session['update_tournament'] = tournament.id
        else:
            is_creator = False

        return render(request, 'tournaments/a_tournament.html', {
            'tournament': tournament,
            'creator': tournament.creator_name,
            'teams': registered_teams,
            'slots': int(tournament.team_numbers) - registered_teams.count(),
            'is_creator': is_creator
        })

    def post(self, request):
        pass


# Update tournament for the creator of the tournament only
class UpdateTournamentView(View):
    def get(self, request, slug):
        form = UpdateTournamentsForm()
        tournament = TournamentsModel.objects.get(slug=slug)
        return render(request, 'tournaments/update_tournament.html', {
            'form': form,
            'tournament': tournament
        })

    def post(self, request, slug):
        tournament = TournamentsModel.objects.get(slug=slug)
        form = UpdateTournamentsForm(request.POST)
        if form.is_valid():
            tournament.tournament_name = form.cleaned_data['tournament_name']
            tournament.your_email = form.cleaned_data['your_email']
            tournament.fee = form.cleaned_data['fee']
            tournament.team_numbers = form.cleaned_data['team_numbers']
            tournament.save()
            return redirect('a-tournament', tournament.slug)


class RegisterTournamentView(View):
    def get(self, request, slug):
        already_registered = False
        leader_id = request.session['user_id']

        # print(slug)
        tournament = TournamentsModel.objects.get(slug=slug)
        already_registered_teams = tournament.teams.all()
        for team in already_registered_teams:
            if team.leader.id == leader_id:
                already_registered = True
        request.session['tournament_id'] = tournament.id
        form = TournamentRegisterForm()
        return render(request, 'tournaments/register_a_tournament.html', {
            'form': form,
            'slug': tournament.slug,
            'already_registered': already_registered

        })

    def post(self, request, slug):
        team = TournamentRegisterForm(request.POST)
        user_id = request.session['user_id']
        # tournament = request.session['tournament_id']
        if team.is_valid():
            team_model = TeamsModel(team_name=team.cleaned_data['team_name'], player1=team.cleaned_data['player1'],
                                    player2=team.cleaned_data['player2'],
                                    player3=team.cleaned_data['player3'], player4=team.cleaned_data['player4'],
                                    leader=UserModel.objects.get(id=user_id),
                                    tournament=TournamentsModel.objects.filter(slug=slug)[0])

            team_model.save()
            return redirect('a-tournament', slug)
        return render(request, 'tournaments/register_a_tournament.html', {
            'form': team,
            'slug': slug
        })
