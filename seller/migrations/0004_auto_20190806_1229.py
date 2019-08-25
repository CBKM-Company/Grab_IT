# Generated by Django 2.2.4 on 2019-08-06 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='seller.Seller'),
        ),
    ]
