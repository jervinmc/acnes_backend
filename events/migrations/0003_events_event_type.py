# Generated by Django 4.0.1 on 2022-01-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_events_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_type',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='event_type'),
        ),
    ]
