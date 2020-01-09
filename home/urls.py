from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('logout/', views.logout_view, name='logout'),
]




