# Generated by Django 4.0.4 on 2022-05-17 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='last_job',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='soft_skills',
        ),
    ]
