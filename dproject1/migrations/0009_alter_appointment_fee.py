# Generated by Django 5.0.6 on 2024-06-10 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dproject1', '0008_appointment_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='fee',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
