# Generated by Django 4.0 on 2022-01-11 02:22

from django.db import migrations, models
import marketplace.models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_marketplace_user_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marketplace',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='marketplace',
            name='image_qr',
            field=models.ImageField(default='uploads/image_qr.png', upload_to=marketplace.models.nameFile, verbose_name='image_qr'),
        ),
    ]
