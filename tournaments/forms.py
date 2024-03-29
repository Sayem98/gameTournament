from django import forms

# Create your forms here

game_type_choices = (('PUBG', 'PUBG'),
                     ('Sea of Theves', 'Sea of Theves'),
                     ('Call of duty', 'Call of Duty'))


class TournamentsForm(forms.Form):
    game_type = forms.ChoiceField(choices=game_type_choices)
    tournament_name = forms.CharField(max_length=30, label='Tournament Name')
    your_email = forms.EmailField(label='Your Email')
    fee = forms.CharField(max_length=5, label='Fee')
    team_numbers = forms.CharField(max_length=2)
    last_register_date = forms.DateField(label='Last Registration date')


class UpdateTournamentsForm(forms.Form):
    # game_type = forms.ChoiceField(choices=game_type_choices)
    tournament_name = forms.CharField(max_length=30, label='Tournament Name')
    your_email = forms.EmailField(label='Your Email')
    fee = forms.CharField(max_length=5, label='Fee')
    team_numbers = forms.CharField(max_length=2)


class TournamentRegisterForm(forms.Form):
    team_name = forms.CharField(max_length=20)
    player1 = forms.CharField(max_length=10)
    player2 = forms.CharField(max_length=10)
    player3 = forms.CharField(max_length=10)
    player4 = forms.CharField(max_length=10)

