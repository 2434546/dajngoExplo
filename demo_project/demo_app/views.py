from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class index_view(View):
    def get(self, request):
        return render(request, 'index.html')

class login_view(View):
    def get(self, request):
        return render(request, 'login.html')

class reservations_view(View):
    def get(self, request):
        return render(request, 'reservations.html')

class liste_voitures_view(View):
    def get(self, request):
        return render(request, 'liste_voitures.html')