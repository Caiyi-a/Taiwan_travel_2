# Generated by Django 5.0 on 2024-01-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activityimage',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
