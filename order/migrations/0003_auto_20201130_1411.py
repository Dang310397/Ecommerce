# Generated by Django 2.2 on 2020-11-30 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
