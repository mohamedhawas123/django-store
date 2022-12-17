# Generated by Django 4.1.3 on 2022-12-17 14:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_addressuser_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressuser',
            name='date',
        ),
        migrations.AddField(
            model_name='addressuser',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addressuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
