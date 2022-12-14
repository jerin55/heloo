# Generated by Django 4.0.5 on 2022-07-27 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_test_pr2_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('price', models.FloatField(default=0.0)),
                ('product_available_count', models.IntegerField(default=0)),
                ('img', models.ImageField(null=True, upload_to='images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
    ]
