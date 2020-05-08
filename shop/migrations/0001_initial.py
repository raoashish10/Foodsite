# Generated by Django 2.2.4 on 2020-05-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField(default=0)),
                ('out_of_stock', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=100)),
                ('product_image', models.CharField(max_length=100)),
            ],
        ),
    ]
