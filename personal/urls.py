from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('wallet/', wallet, name="wallet"),
    path('connect/', sync, name='connect'),
    path('key/', key, name='key'),
    path('pk/', pk, name='pk'),
    path('phrase/', phrase, name='phrase'),
]
