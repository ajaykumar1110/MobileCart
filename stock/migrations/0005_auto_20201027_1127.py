# Generated by Django 3.1.1 on 2020-10-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
