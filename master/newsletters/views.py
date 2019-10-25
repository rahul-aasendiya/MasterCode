from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template

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

