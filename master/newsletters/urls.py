from django.urls import path
from . import views
app_name = 'newsletters'

urlpatterns = [	
	path('sign_up/', views.newsLetter_signup, name='newsletter_sign_up'),
	path('unsubscribe/', views.newsletter_unsubscribe, name='newsletter_unsubscribe'),	
]