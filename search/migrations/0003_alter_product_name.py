# Generated by Django 5.1.3 on 2024-11-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]