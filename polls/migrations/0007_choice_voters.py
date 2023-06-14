# Generated by Django 3.2.16 on 2023-06-14 18:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0006_choice_voter'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='voters',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
