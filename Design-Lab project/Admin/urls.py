from django.urls import path
from . import views

urlpatterns = [
    path('adminhome/', views.adminHomePage, name='adminHomePage'),
    path('adminlogin/', views.adminLoginPage, name='adminLoginPage'),
    path('adminlogout/', views.LogOut, name='LogOut'),
    path('adminlogindetails/', views.adminSuper, name='adminSuper'),
    path('approvearchitect/', views.approveArchitect, name='approveArchitect'),
    path('approvedesigner/', views.approveDesigner, name='approveDesigner'),
    path('managearchitect/', views.manageArchitect, name='manageArchitect'),
    path('managedesigner/', views.manageDesigner, name='manageDesigner'),
    path('workwithuslogin/', views.workWithUsLogin, name='workWithUsLogin'),
    path('workwithusregister/', views.workWithUsRegister, name='workWithUsRegister'),
    path('registerarchdes/', views.RegisterArchitectDesigner, name='RegisterArchitectDesigner'),
    path('viewData/<int:dataid>', views.viewData, name='viewData'),
    path('viewData1/<int:dataid>', views.viewData1, name='viewData1'),
    path('viewma/<int:dataid>', views.viewMA, name='viewMA'),
    path('viewmd/<int:dataid>', views.viewMD, name='viewMD'),
    path('deletearchitect/<int:dataid>', views.deleteArchitect, name='deleteArchitect'),
    path('deletedesigner/<int:dataid>', views.deleteDesigner, name='deleteDesigner'),
]