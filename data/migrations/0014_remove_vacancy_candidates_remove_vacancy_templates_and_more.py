# Generated by Django 4.2.23 on 2025-07-18 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_vacancy_templates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='candidates',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='templates',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='vacancies',
            field=models.ManyToManyField(blank=True, related_name='candidates', to='data.vacancy'),
        ),
        migrations.AlterField(
            model_name='template',
            name='vacancies',
            field=models.ManyToManyField(blank=True, related_name='templates', to='data.vacancy'),
        ),
    ]
