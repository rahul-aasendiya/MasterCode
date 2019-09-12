from django.contrib import admin
from .models import NewsLetterUser, NewsLetter

class NewsLetterUserAdminModel(admin.ModelAdmin):
	list_display = ['email','date_added']
	class Meta:
		model = NewsLetterUser

admin.site.register(NewsLetterUser, NewsLetterUserAdminModel)

admin.site.register(NewsLetter)