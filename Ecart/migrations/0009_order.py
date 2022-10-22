# Generated by Django 4.1.2 on 2022-10-22 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecart', '0008_carts_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('ordred_date', models.DateTimeField(auto_now_add=True)),
                ('order_items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Ecart.carts')),
            ],
        ),
    ]
