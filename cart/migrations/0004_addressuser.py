# Generated by Django 4.1.3 on 2022-12-17 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0003_cartitem_user_alter_cartitem_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=245)),
                ('last_name', models.CharField(max_length=245)),
                ('email', models.EmailField(max_length=245)),
                ('phone_number', models.CharField(max_length=245)),
                ('address_line', models.CharField(max_length=245)),
                ('city', models.CharField(max_length=245)),
                ('state', models.CharField(max_length=245)),
                ('country', models.CharField(max_length=245)),
                ('order_note', models.TextField()),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_cart', to='cart.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_addrss', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
