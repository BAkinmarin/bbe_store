# Generated by Django 5.1.10 on 2025-06-14 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
