# Generated by Django 4.0.1 on 2022-01-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_events_no_going_events_no_interested'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='events',
            name='event_end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='event_end_date'),
        ),
        migrations.AlterField(
            model_name='events',
            name='event_start_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='event_start_date'),
        ),
    ]