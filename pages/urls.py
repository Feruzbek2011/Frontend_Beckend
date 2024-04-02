from django.urls import path
from .views import *

urlpatterns = [
    path('home', HomePageView.as_view(), name='home'),
    path('devoloper/', HomeDevoloperView.as_view(), name='devoloper'),
    path('yoriqnoma/', HomeSignuploginView.as_view(), name='yoriqnoma'),
    path('logintest/', HomeLogintestView.as_view(), name='logintest'),
]
