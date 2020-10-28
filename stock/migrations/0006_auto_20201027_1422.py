# Generated by Django 3.1.1 on 2020-10-27 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20201027_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='customer_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]