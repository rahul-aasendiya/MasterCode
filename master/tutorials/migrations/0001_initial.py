# Generated by Django 2.2.5 on 2019-09-12 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StudentExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advance', 'Advance')], default='Beginner', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TutorialSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.Language')),
                ('student_experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorials.StudentExperience')),
            ],
        ),
        migrations.CreateModel(
            name='Lession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('video', models.TextField(blank=True, null=True)),
                ('length', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('free_preview', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('tutorial_series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutorials', to='tutorials.TutorialSeries')),
            ],
        ),
    ]
