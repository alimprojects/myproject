# Generated by Django 5.0.3 on 2024-03-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0012_shipper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('SupplierID', models.AutoField(primary_key=True, serialize=False)),
                ('SupplierName', models.CharField(max_length=255)),
                ('ContactName', models.CharField(max_length=255)),
                ('Address', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=100)),
                ('PostalCode', models.CharField(max_length=20)),
                ('Country', models.CharField(max_length=100)),
            ],
        ),
    ]