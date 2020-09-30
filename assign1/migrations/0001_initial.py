# Generated by Django 3.0.8 on 2020-08-31 19:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('dob', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('gender', models.CharField(max_length=2)),
                ('date_created', models.DateTimeField()),
            ],
        ),
    ]