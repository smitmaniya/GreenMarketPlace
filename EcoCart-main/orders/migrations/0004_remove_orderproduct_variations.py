# Generated by Django 5.0.7 on 2024-07-11 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210616_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variations',
        ),
    ]
