from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view.as_view(), name="index"),
    path('login/', views.login_view.as_view(), name="login"),
    path('reservations/', views.reservations_view.as_view(), name="reservations"),
    path('voitures/', views.liste_voitures_view.as_view(), name="liste_voitures"),
]