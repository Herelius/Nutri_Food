# Generated by Django 5.1.3 on 2024-11-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('ingredient', models.CharField(max_length=250)),
                ('nutri_score', models.CharField(max_length=1)),
                ('image', models.URLField()),
            ],
        ),
    ]
