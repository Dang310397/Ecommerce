# Generated by Django 2.2 on 2020-12-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count_sold',
            field=models.IntegerField(default=0),
        ),
    ]
