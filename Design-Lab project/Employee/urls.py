from django.urls import path
from . import views



urlpatterns = [
    path('architecthome/', views.architectHome, name='architectHome'),
    path('designerhome/', views.designerHome, name='designerHome'),
    path('addplan/', views.addPlan, name='addPlan'),
    path('adddesign/', views.addDesign, name='addDesign'),
    path('employeelogin/', views.employeeLogin, name='employeeLogin'),
    path('viewaplans/', views.viewAplans, name='viewAplans'),
    path('viewdplans/', views.viewDplans, name='viewDplans'),
    path('saveplans/', views.savePlan, name='savePlan'),
    path('savedesigns/', views.saveDesign, name='saveDesign'),
    path('editplan/<int:plan_id>', views.editPlan, name='editPlan'),
    path('editdesign/<int:design_id>', views.editDesign, name='editDesign'),
    path('updateplan/<int:plan_id>', views.updatePlan, name='updatePlan'),
    path('updatedesign/<int:design_id>', views.updateDesign, name='updateDesign'),
    path('deleteplan/<int:plan_id>', views.deletePlan, name='deletePlan'),
    path('deletedesign/<int:design_id>', views.deleteDesign, name='deleteDesign'),
]