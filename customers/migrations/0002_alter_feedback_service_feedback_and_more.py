# Generated by Django 4.0 on 2022-02-08 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='service_feedback',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
