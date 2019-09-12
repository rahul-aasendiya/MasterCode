from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template

from .models import NewsLetterUser, NewsLetter
from .forms import NewsLetterFormSignUpForm, NewsLetterCreationForm

def newsLetter_signup(request):
	form = NewsLetterFormSignUpForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		if NewsLetterUser.objects.filter(email=instance.email).exists():
			messages.warning(request, "your email already exists in our database.", "alert alert-warning alert-dismissible")

		else:
			instance.save()
			messages.success(request, "Your email has been submitted to the database","alert alert-success alert-dismissible")
			subject = "Thank you for joining our newsletter."
			from_email = settings.EMAIL_HOST_USER
			to_email = [instance.email]

			with open(settings.BASE_DIR + "/templates/website/newsletters/sign_up_email.txt") as f:
				signup_message = f.read()
			message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
			html_template = get_template('website/newsletters/sign_up_email.html').render()
			message.attach_alternative(html_template, 'text/html')
			message.send(fail_silently=True)
	context = {
		'form':form,
	}
	return render(request, 'website/newsletters/sign_up.html', context)

		
def newsletter_unsubscribe(request):
	form = NewsLetterFormSignUpForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		if NewsLetterUser.objects.filter(email=instance.email).exists():
			NewsLetterUser.objects.filter(email=instance.email).delete()
			messages.success(request, "your email has been removed.", "alert alert-success alert-dismissible")

			subject = "You have been unsubscribed"
			from_email = settings.EMAIL_HOST_USER
			to_email = [instance.email]

			with open(settings.BASE_DIR + "/templates/website/newsletters/unsubscribe_email.txt") as f:
				signup_message = f.read()
			message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
			html_template = get_template('website/newsletters/unsubscribe_email.html').render()
			message.attach_alternative(html_template, 'text/html')
			message.send(fail_silently=True)
		else:
			messages.warning(request, "your email is not in our database.", "alert alert-warning alert-dismissible")
	
	context = {
		'form':form,
	}
	return render(request, 'website/newsletters/unsubscribe.html', context)

def control_newsletter(request):
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
			return redirect('control_panel:control_newsletter_list')
		else:
			messages.success(request, "Add newsletter successfully as draft.","alert alert-success alert-dismissible")
			return redirect('control_panel:control_newsletter_list')
	context = {
		'form':form,
	}
	return render(request, 'control_panel/control_newsletter.html', context)

def control_newsletter_list(request):
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
		'items':items
	}
	return render(request, 'control_panel/control_newsletter_list.html', context)

def control_newsletter_detail(request, pk):
	newsletter = get_object_or_404(NewsLetter, pk=pk)
	context = {
		'newsletter':newsletter
	}
	return render(request, 'control_panel/control_newsletter_detail.html', context)

def control_newsletter_edit(request, pk):
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
			return redirect('control_panel:control_newsletter_detail', pk=newsletter.pk)
	else:
		form = NewsLetterCreationForm(instance=newsletter)
	context = {
		'newsletter':newsletter,
		'form':form,
	}
	return render(request, 'control_panel/control_newsletter.html', context)

def control_newsletter_delete(request, pk):
	newsletter = get_object_or_404(NewsLetter, pk=pk)

	if request.method == "POST":
		form = NewsLetterCreationForm(request.POST, instance=newsletter)

		if form.is_valid():
			subject = newsletter.subject
			messages.success(request, f"{subject} has beed deleted!","alert alert-success alert-dismissible")
			newsletter.delete()
			return redirect('control_panel:control_newsletter_list')
	else:
		form = NewsLetterCreationForm(instance=newsletter)
	context = {
		'form':form,
	}
	return render(request, 'control_panel/control_newsletter_delete.html', context)