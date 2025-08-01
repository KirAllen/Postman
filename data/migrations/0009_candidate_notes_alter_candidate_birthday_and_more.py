# Generated by Django 4.2.23 on 2025-07-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_candidate_email_candidate_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='birthday',
            field=models.DateField(blank=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='firstname',
            field=models.CharField(blank=True, max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='patronymic',
            field=models.CharField(blank=True, max_length=100, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='surname',
            field=models.CharField(blank=True, max_length=100, verbose_name='Фамилия'),
        ),
    ]
