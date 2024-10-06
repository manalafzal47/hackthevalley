from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('callback', views.callback, name="callback"),
    path('register', views.registration_page, name='registration_page'),
    path('market', views.market, name='market'),
    path('shopping', views.shopping, name='shopping')
]