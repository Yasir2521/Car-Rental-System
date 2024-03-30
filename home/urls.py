from django.contrib import admin
from django.urls import path
from home import views

from django.urls import register_converter
from . import converters

register_converter(converters.FloatConverter, 'float')

urlpatterns = [
    path('', views.index, name = 'home'),
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('loggedin', views.loggedin, name = 'loggedin'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('editted', views.editted, name='editted'),

    path('contact/',views.contact,name = 'contact'),

    path('vehicles.html', views.vehicles, name='vehicles'),
    
    path('car_history/<int:car_id>/', views.car_history, name='car_history'),
    
    path("bill",views.bill,name = "bill"),
    path("order",views.order,name = "order"),
    path("about.html",views.about_us, name='about_us'),
    path("rent_history.html",views.rent_history, name='rent_history'),
    path('payment/<int:order_id>/<float:total_rent>/', views.payment, name='payment'),
    path('review.html',views.review,name ='review'), 

    
]