from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('A/', views.A, name='A'),
    path('D/', views.D, name='D'),
    path('customerrl/', views.customerRLpage, name='customerRLpage'),
    path('customersave/', views.customerSaveData, name='customerSaveData'),
    path('customerlogin/', views.customerLogin, name='customerLogin')
]