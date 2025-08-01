# Generated by Django 4.2.23 on 2025-07-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_vacancy_candidates_vacancy_templates_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='vacancies',
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='candidates',
            field=models.ManyToManyField(blank=True, related_name='vacancies', to='data.candidate'),
        ),
    ]
