from django.shortcuts import render
from tutorials.models import TutorialSeries

def index(request):
	tutorial_series_list = TutorialSeries.objects.filter(archived=True).order_by('-id')[:3]
	context = {
		'object_list':tutorial_series_list,
	}
	return render(request, 'website/index.html', context)