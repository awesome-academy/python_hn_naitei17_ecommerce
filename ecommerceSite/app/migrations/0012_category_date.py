# Generated by Django 4.2.1 on 2023-05-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_order_shipping_address_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
