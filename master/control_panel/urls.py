from django.urls import path
from newsletters.views import (
	control_newsletter,
	control_newsletter_list,
	control_newsletter_detail,
	control_newsletter_edit,
	control_newsletter_delete
	)

app_name = 'control_panel'

urlpatterns = [	
	path('', control_newsletter_list, name='control_newsletter_list'),
	path('newsletters/', control_newsletter, name='control_newsletter'),	
	path('newsletters/detail/<int:pk>/', control_newsletter_detail, name='control_newsletter_detail'),	
	path('newsletters/edit/<int:pk>/', control_newsletter_edit, name='control_newsletter_edit'),	
	path('newsletters/delete/<int:pk>/', control_newsletter_delete, name='control_newsletter_delete'),	
]