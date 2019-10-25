from django.urls import path
from . import views

app_name = 'control_panel'

urlpatterns = [	
	path('', views.dashboard, name='dashboard'),
	path('newsletters/', views.newsletter_list, name='newsletter_list'),
	path('newsletter/create/', views.create_newsletter, name='create_newsletter'),	
	path('newsletter/detail/<int:pk>/', views.newsletter_detail, name='newsletter_detail'),	
	path('newsletter/edit/<int:pk>/', views.newsletter_edit, name='newsletter_edit'),	
	path('newsletter/delete/<int:pk>/', views.newsletter_delete, name='newsletter_delete'),	
]