# Generated by Django 5.1.1 on 2024-10-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_homework_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='subject',
            field=models.CharField(default='Default Subject', max_length=50),
        ),
    ]
