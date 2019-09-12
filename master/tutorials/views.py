from django.shortcuts import render, get_object_or_404
from .models import TutorialSeries, Lession
from django.db.models import Count

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def tutorial_series_list(request):
	tutorials = TutorialSeries.objects.all().prefetch_related('tutorials')
	tutorials = tutorials.annotate(lession=Count('tutorials'))

	paginator = Paginator(tutorials, 2)
	page = request.GET.get('page')
	try:
		items = paginator.page(page)
	except PageNotAnInteger:
		items = paginator.page(1)
	except EmptyPage:
		items = Paginator.page(paginator.num_page)

	index = items.number - 1
	max_index = len(paginator.page_range)
	start_index = index - 5 if index >= 5 else 0
	end_index = index + 5 if index <= max_index - 5 else max_index
	page_range = paginator.page_range[start_index:end_index]


	context = {
		'tutorials':tutorials,
		'page_range':page_range,
		'items':items
	}
	return render(request, 'website/tutorial_series_list.html', context)

def tutorial_series_detail(request, slug):
	tutorial_series = get_object_or_404(TutorialSeries, slug=slug)
	lessions_list = tutorial_series.tutorials.filter(tutorial_series=tutorial_series)
	# lessions_list = tutorial_series.lession_set.filter(tutorial_series=tutorial_series)
	# lessions_list = Lession.objects.filter(tutorial_series=tutorial_series)
	context = {
		'object': tutorial_series,
		'lessions': lessions_list
	}
	return render(request, 'website/tutorial_series_detail.html', context)

def lession_detail(request, tutorial_series, slug):
	lession = get_object_or_404(Lession.objects.filter(tutorial_series__slug=tutorial_series, slug=slug))
	context = {
		'lession':lession,
	}
	return render(request, 'website/tutorials/tutorial_detail.html', context)
