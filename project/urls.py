from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('dashboard/login', views.login, name="login"),
    path('dashboard/', views.news, name="dashboard"),
    path('category/', views.category, name="category"),
    path('dashboard/Business/',views.business, name="business"),
    path('dashboard/entertainment/',views.entertainment, name="entertainment"),
    path('dashboard/health/',views.health, name="health"),
    path('dashboard/sports/',views.sports, name="sports"),
    path('dashboard/science/',views.science, name="science"),
    path('dashboard/technology/',views.technology, name="technology"),
    path('dashboard/general/',views.general, name="general"),
    path('dashboard/search/',views.search,name="search"),
    path('profile/',views.profile,name="profile"),
    # path('home/',views.home, name="home"),
]
