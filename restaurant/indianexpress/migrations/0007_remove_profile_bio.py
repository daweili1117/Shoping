# Generated by Django 2.2 on 2020-03-12 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indianexpress', '0006_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
