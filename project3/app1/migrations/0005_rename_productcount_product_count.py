# Generated by Django 4.0.5 on 2022-07-27 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_product_available_count_product_productcount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productcount',
            new_name='count',
        ),
    ]