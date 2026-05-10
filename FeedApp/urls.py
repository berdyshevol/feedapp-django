from django.urls import path
from . import views

app_name = 'FeedApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('myfeed', views.myfeed, name='myfeed'),
    path('new_prost/', views.new_post, name='new_post'),
    ]

    