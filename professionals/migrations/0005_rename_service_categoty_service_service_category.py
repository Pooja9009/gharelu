# Generated by Django 4.0 on 2022-02-04 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0004_alter_service_service_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_categoty',
            new_name='service_category',
        ),
    ]
