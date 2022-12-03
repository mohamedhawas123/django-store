# Generated by Django 4.1.3 on 2022-12-03 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_account_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
