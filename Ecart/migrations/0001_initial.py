# Generated by Django 4.1.2 on 2022-10-20 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('prodect_image', models.ImageField(null=True, upload_to='prodects_img/')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('in_stock', models.IntegerField()),
                ('out_of_stock', models.CharField(choices=[('no stock', 'out of stock'), ('Stocks available', 'stock available')], max_length=40, null=True)),
            ],
        ),
    ]
