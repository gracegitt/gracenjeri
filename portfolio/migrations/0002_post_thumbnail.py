# Generated by Django 4.1.5 on 2023-02-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='placeholder.jpg', null=True, upload_to='images'),
        ),
    ]
