# Generated by Django 4.0 on 2021-12-23 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0012_usersignup_delete_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserSignUp',
        ),
    ]
