from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('details/',views.details,name='details'),
    path('department/',views.department,name='department'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('logout',views.logout,name='logout'),



]