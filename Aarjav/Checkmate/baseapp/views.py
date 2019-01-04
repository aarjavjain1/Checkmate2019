from django.shortcuts import render
from .models import Team, UserInfo
from django.http import HttpResponse
from django.contrib.auth.models import User
#from django.contrib.auth import authenticate
# Create your views here.

def leaderboard(request):
    team = Team.objects.order_by('-score')
    return render(request, 'baseapp/leaderboard.html', {'all_teams': team})

def selectTeam(request):
    team = Team.objects.all()
    #team = Team.objects.get(number_of_players=1)

    if request.method == 'POST':
        print('Request Sent!')
        teamname = radiobutton
        user.team = teamname
        for t in team:
            if t.team_name == teamname:
                t.number_of_players += 1
                break

    return render(request, 'baseapp/selectTeam.html', {'listofteams': team})


def afterTeam(request):
    if request.method == 'POST':
        #team = request['POST'].get('team')
        team = request.POST.get('team')
        teammate_email = request.POST.get('teammate')
        teammate = teammate_email.split('@')[0]
        users_all = User.objects.all()
        teams_all = Team.objects.all()
        Team_exists = False
        Teammate_exists = False


        for myteam in teams_all:
            if team == myteam.team_name:
                Team_exists = True
                team_id = myteam.pk
                print('team exists')

        for user in users_all:
            if user.username == teammate:
                Teammate_exists = True
                userinfo = UserInfo.objects.get_or_create(user=user, team_id=team_id)[0]
                print('teammate exists')

        current_user = request.user
        print(current_user.username)
        userinfo2 = UserInfo.objects.get_or_create(user=current_user, team_id=team_id)[0]


        if Team_exists and Teammate_exists:
            return HttpResponse('Your Team is '+team+' and your Teammate is '+teammate)
        else:
            return HttpResponse('Your Teammate is not registered!')
