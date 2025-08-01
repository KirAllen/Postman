# Generated by Django 4.2.23 on 2025-07-12 12:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_alter_candidate_options_alter_candidate_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('interview', 'Назначено собеседование'), ('accepted', 'Принят'), ('rejected', 'Отклонен')], default='new', max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='birthday',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cvs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Резюме'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='patronymic',
            field=models.CharField(max_length=100, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='surname',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
    ]
