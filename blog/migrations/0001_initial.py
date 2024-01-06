# Generated by Django 5.0 on 2024-01-06 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_photos/')),
                ('text', models.CharField(max_length=255)),
            ],
        ),
    ]
