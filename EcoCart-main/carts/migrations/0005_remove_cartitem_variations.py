# Generated by Django 5.0.7 on 2024-07-11 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20210614_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='variations',
        ),
    ]