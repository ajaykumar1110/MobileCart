# Generated by Django 3.1.1 on 2020-10-22 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='datecReceived',
            new_name='dateReceived',
        ),
    ]
