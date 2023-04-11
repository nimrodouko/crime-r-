from django.urls import path
from .views import *
from . import views

urlpatterns=[
   path('', HomeView.as_view(),name='home'),
   path('about/', AboutView.as_view(),name='about'),
  
   path('reports/',views.report,name='report'),
   path('wanted/', WantedView.as_view(),name='wanted'),
   path('edits/<int:id>/', views.report_edit,name='edits'),
   
   path('delete/<id>/',views.report_delete,name='delete'),
   path('cases/',views.case_list,name='cases'),
   path('send/', views.send_email, name = 'mail'),
    path('email/', EmailView.as_view(),name='email'),
   
  

]