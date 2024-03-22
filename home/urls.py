from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('loggedin', views.loggedin, name = 'loggedin'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('editted', views.editted, name='editted'),
    path('property_det', views.property_det, name='property_det'),
    path('contact/',views.contact,name = 'contact'),
    #path("vehicles/", views.vehicles, name= "vehicles"),
    path('vehicles.html', views.vehicles, name='vehicles'),
    #path('bill.html', views.bill, name='bill'),
    path('car_history/<int:car_id>/', views.car_history, name='car_history')

]