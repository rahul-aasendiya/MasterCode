from django.contrib import admin
from .models import Language, StudentExperience, TutorialSeries, Lession


class LanguageAdminModel(admin.ModelAdmin):
	list_display = ["name", "active"]
	list_filter = ["name"]
	search_fields = ["name", "description"]
	prepopulated_fields = {'slug':('name',)}

	class Meta:
		model = Language
admin.site.register(Language, LanguageAdminModel)


# class StudentExperienceAdminModel(admin.ModelAdmin):
# 	list_display = ['experience_level']
# 	list_filter = ['experience_level']
# 	search_fields = ['experience_level']

# 	class Meta:
# 		model = StudentExperience
# admin.site.register(StudentExperience, StudentExperienceAdminModel)


class TutorialSeriesAdminModel(admin.ModelAdmin):
	list_display = ["name", "archived"]
	list_filter = ["language", "language", "student_experience", "archived"]
	search_fields = ["name", "description"]
	prepopulated_fields = {'slug':('name',)}

	class Meta:
		model = TutorialSeries
admin.site.register(TutorialSeries, TutorialSeriesAdminModel)


class LessionSeriesAdminModel(admin.ModelAdmin):
	list_display = ["title", "free_preview", "active"]
	list_filter = ["free_preview", "active"]
	search_fields = ["title", "content"]
	prepopulated_fields = {'slug':('title',)}

	class Meta:
		model = Lession
admin.site.register(Lession, LessionSeriesAdminModel)