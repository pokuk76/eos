from django.urls import path
from django.views.generic.base import TemplateView # new

from . import views

#from django.conf.urls import url

app_name = 'portal'

urlpatterns = [

    #path('login/', views.login, name='login'),
    path('nhis_form/', views.nhis_form, name='nhis_form'),
    path('pocket_guide/', views.pocket_guide, name='pocket_guide'),
    path('personal_details/', views.personal_details, name='personal_details'),
    path('', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('is/', views.ISView.as_view(), name='is'),
    path('hr/', views.HRView.as_view(), name='hr'),
    path('employees/', views.EmployeesView.as_view(), name='employees'),
    path('forms/', views.FormsView.as_view(), name='forms'),
    path('todo/', views.TodoView.as_view(), name='todo'),
    path('tutorials/', views.TutorialsView.as_view(), name='tutorials'),

]
