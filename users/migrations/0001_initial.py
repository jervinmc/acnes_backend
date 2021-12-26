# Generated by Django 4.0 on 2021-12-18 20:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(blank=True, default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_joined')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('lastname', models.CharField(blank=True, max_length=255, verbose_name='lastname')),
                ('contact_number', models.CharField(blank=True, max_length=255, verbose_name='contact_number')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='address')),
                ('password', models.CharField(blank=True, max_length=255, verbose_name='password')),
                ('email', models.CharField(blank=True, max_length=255, unique=True, verbose_name='email')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('account_type', models.CharField(blank=True, max_length=255, verbose_name='account_type')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
