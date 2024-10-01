from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view.as_view(), name="index"),
]