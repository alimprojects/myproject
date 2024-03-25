# Generated by Django 5.0.3 on 2024-03-20 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0014_supplier_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
