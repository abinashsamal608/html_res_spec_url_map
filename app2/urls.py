from django.urls import path
from app2.views import *
app_name = 'two'

urlpatterns=[
    path('third/', third, name='third'),
    path('fourth/', fourth, name = 'fourth'),
]
