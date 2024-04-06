from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.generate_timestamp, name='generate_timestamp'),
]