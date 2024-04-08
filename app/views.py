from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from .team_info import TEAM

# Create your views here.
def team_view(request):
    # context = {"Team":TEAM}
    return render(request, "home.html",{"Team":TEAM})

def team_deets(request,name):
    return render(request, "teamdeets.html" )