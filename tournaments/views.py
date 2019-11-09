import json
from django.shortcuts import render, redirect
import requests
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from tournaments.forms import TournamentJoin


def tournament_list(request):
    url = 'http://127.0.0.1:8000/api/tournaments/'
    response = requests.get(url)
    tournaments = response.json()
    print(tournaments)
    return render(request, 'tournaments/show_tournaments.html', {'tournaments': tournaments})


def join_tournament(request, pk, t_name, start_date, end_date, location):
    if request.method == 'POST':
        form = TournamentJoin(request.POST)
        if form.is_valid():
            url = 'http://127.0.0.1:8000/api/tournaments_join/'
            k = request.POST['pk']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            if form.cleaned_data['phone_number']:
                phone_num = form.cleaned_data['phone_number']
                data = json.dumps({'name': name, 'tournament': k, 'mail': email, 'phoneNumber': phone_num})
                requests.post(url=url, data=data)

            else:
                data = json.dumps({'name': name, 'tournament': k, 'mail': email})
                requests.post(url=url, data=data)

            current_site = get_current_site(request)
            mail_subject = 'SportsHub Tournament Registration Confirmation'
            message = render_to_string('tournaments/activate_email.html', {
                'domain': current_site.domain,
                'user': name,
                'start_date': start_date,
                'end_date': end_date,
                'location': location,
                'tournament_name': t_name
            })
            email = EmailMessage(
                mail_subject, message, to=[email]
            )
            email.send()
            return redirect('tournaments:tournament_list')

        else:
            print('form is invalid')
            print(form.errors)
    else:
        form = TournamentJoin()

    print(int(pk))
    return render(request, 'tournaments/join_tournament.html', {'form': form, 'pk': int(pk)})
