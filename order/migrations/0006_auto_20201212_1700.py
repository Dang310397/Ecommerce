# Generated by Django 2.2 on 2020-12-12 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
