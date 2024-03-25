# Generated by Django 5.0.3 on 2024-03-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0005_customer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CategoryID', models.AutoField(primary_key=True, serialize=False)),
                ('CategoryName', models.CharField(max_length=100)),
                ('Description', models.TextField()),
            ],
        ),
    ]