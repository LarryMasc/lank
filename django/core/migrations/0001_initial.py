# Generated by Django 2.1.3 on 2018-11-27 02:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='email_data',
            fields=[
                ('sender', models.EmailField(max_length=254)),
                ('recipient', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=70)),
                ('body', models.TextField()),
                ('send_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('cc_myself', models.BooleanField()),
                ('email_tag', models.CharField(max_length=32)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
