# Generated by Django 5.0.3 on 2024-06-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]