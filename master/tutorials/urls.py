from django.urls import path
from . import views
app_name = 'tutorials'

urlpatterns = [	
	path('tutorial_series_list/', views.tutorial_series_list, name='tutorial_series_list'),
	path('<str:slug>/', views.tutorial_series_detail, name='tutorial_series_detail'),
	path('<str:tutorial_series>/<str:slug>/', views.lession_detail, name='lession_detail'),
]