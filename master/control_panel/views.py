from django.conf import settings
from django.shortcuts import render
from newsletters.models import NewsLetterUser, NewsLetter
from newsletters.forms import NewsLetterFormSignUpForm, NewsLetterCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.contrib import messages


def dashboard(request):
	return render(request, 'control_panel/dashboard.html')

def create_newsletter(request):
	form = NewsLetterCreationForm(request.POST or None)

	if form.is_valid():
		instance = form.save()
		newsletter = NewsLetter.objects.get(id=instance.id)
		if newsletter.status == "Published":
			subject = newsletter.subject
			body = newsletter.body
			from_email = settings.EMAIL_HOST_USER
			for email in newsletter.email.all():
				send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)
			messages.success(request, "Add newsletter successfully!","alert alert-success alert-dismissible")
			return redirect('control_panel:newsletter_list')
		else:
			messages.success(request, "Add newsletter successfully as draft.","alert alert-success alert-dismissible")
			return redirect('control_panel:newsletter_list')
	context = {
		'form':form,
	}
	return render(request, 'control_panel/create_newsletter.html', context)

def newsletter_list(request):
	newsletter = NewsLetter.objects.all()

	paginator = Paginator(newsletter, 5)
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
		'page_range':page_range,
		'items':items,
	}
	return render(request, 'control_panel/newsletter_list.html', context)

def newsletter_detail(request, pk):
	newsletter = get_object_or_404(NewsLetter, pk=pk)
	context = {
		'newsletter':newsletter
	}
	return render(request, 'control_panel/newsletter_detail.html', context)

def newsletter_edit(request, pk):
	newsletter = get_object_or_404(NewsLetter, pk=pk)

	if request.method == "POST":
		form = NewsLetterCreationForm(request.POST, instance=newsletter)
		if form.is_valid():
			newsletter = form.save()
			if newsletter.status == "Publish":
				subject = newsletter.subject
				body = newsletter.body
				from_email = settings.EMAIL_HOST_USER
				for email in newsletter.email.all():
					send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=True)
				messages.success(request, "newsletter update successfully!","alert alert-success alert-dismissible")
			return redirect('control_panel:newsletter_detail', pk=newsletter.pk)
	else:
		form = NewsLetterCreationForm(instance=newsletter)
	context = {
		'newsletter':newsletter,
		'form':form,
	}
	return render(request, 'control_panel/create_newsletter.html', context)

def newsletter_delete(request, pk):
	newsletter = get_object_or_404(NewsLetter, pk=pk)

	if request.method == "POST":
		form = NewsLetterCreationForm(request.POST, instance=newsletter)

		if form.is_valid():
			subject = newsletter.subject
			messages.success(request, f"{subject} has beed deleted!","alert alert-success alert-dismissible")
			newsletter.delete()
			return redirect('control_panel:newsletter_list')
	else:
		form = NewsLetterCreationForm(instance=newsletter)
	context = {
		'form':form,
	}
	return render(request, 'control_panel/newsletter_delete.html', context)