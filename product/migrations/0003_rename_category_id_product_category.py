# Generated by Django 4.1.2 on 2022-11-14 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_category_category_id_remove_product_prod_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]
