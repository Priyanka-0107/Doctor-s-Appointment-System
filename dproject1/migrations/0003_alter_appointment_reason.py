# Generated by Django 5.0.6 on 2024-06-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dproject1', '0002_rename_getappointment_appointment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='reason',
            field=models.CharField(default=0, max_length=200000),
        ),
    ]
