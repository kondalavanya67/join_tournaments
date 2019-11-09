from django import forms


class TournamentJoin(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.IntegerField(required=False)
