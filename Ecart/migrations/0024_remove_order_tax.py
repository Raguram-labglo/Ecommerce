# Generated by Django 4.1.2 on 2022-10-28 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecart', '0023_order_tax'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tax',
        ),
    ]
