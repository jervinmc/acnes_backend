# Generated by Django 4.0 on 2021-12-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='is_approved',
            field=models.BooleanField(default=False, verbose_name='is_approved'),
        ),
    ]
