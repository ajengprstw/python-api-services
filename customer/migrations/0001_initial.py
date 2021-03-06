# Generated by Django 3.2.6 on 2021-08-11 09:17

import customer.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=255, verbose_name=customer.models.product)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customers')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('product_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_mode', models.CharField(max_length=255)),
                ('shipping_date', models.DateTimeField()),
                ('shipping_address', models.CharField(max_length=255)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.order')),
            ],
        ),
    ]
