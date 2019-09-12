from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

class Language(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(blank=True, null=True)
	slug = models.SlugField(max_length=250, unique=True)
	active = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Language, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('tutorials:language', args=[self.slug])

	def __str__(self):
		return self.name

class StudentExperience(models.Model):
	EXPERIENCE_LEVEL_CHOICES = (
		('Beginner','Beginner'),
		('Intermediate','Intermediate'),
		('Advance','Advance')
		)

	experience_level = models.CharField(max_length=20, choices=EXPERIENCE_LEVEL_CHOICES, default='Beginner')

	def __str__(self):
		return self.experience_level

class TutorialSeries(models.Model):
	language = models.ForeignKey(Language, on_delete=models.CASCADE)
	student_experience = models.ForeignKey(StudentExperience, on_delete=models.CASCADE)
	name = models.CharField(max_length=250)
	description = models.TextField(blank=True, null=True)
	archived = models.BooleanField(default=False)
	slug = models.SlugField(max_length=250, unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(TutorialSeries, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('tutorials:tutorial_series_detail', args=[self.slug])

	def __str__(self):
		return self.name

class Lession(models.Model):
	tutorial_series = models.ForeignKey(TutorialSeries, related_name='tutorials', on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	video = models.TextField(blank=True, null=True)
	length = models.CharField(max_length=50, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	slug = models.SlugField(max_length=250, unique=True)
	free_preview = models.BooleanField(default=False)
	active = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Lession, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('tutorials:lession_detail', args=[self.slug])

	def __str__(self):
		return self.title

