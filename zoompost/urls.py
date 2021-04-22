from django.urls import path
from .views import registerview,  homeview, intervalview

urlpatterns=[
    path('home/', homeview, name='home'),
    path('interval/', intervalview, name='interval'),
    path('register/<str:date>', registerview, name='register')
]