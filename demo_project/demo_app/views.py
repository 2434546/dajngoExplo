from django.http import Http404
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class index_view(View):
    def get(self, request):
        return render(request, 'index.html')