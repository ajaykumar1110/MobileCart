# Generated by Django 3.1.1 on 2020-10-28 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0012_sold_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sold',
            old_name='user',
            new_name='usersold',
        ),
    ]