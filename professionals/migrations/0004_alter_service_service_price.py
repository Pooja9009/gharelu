# Generated by Django 4.0 on 2022-02-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0003_alter_service_service_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_price',
            field=models.IntegerField(),
        ),
    ]