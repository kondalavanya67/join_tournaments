from django.urls import path
from tournaments import views

app_name = 'tournaments'

urlpatterns = [
    path('tournament_list/', views.tournament_list, name='tournament_list'),
    path('join_tournament/<int:pk>/<str:t_name>/<str:start_date>/<str:end_date>/<str:location>',
         views.join_tournament, name='join_tournament'),
]
