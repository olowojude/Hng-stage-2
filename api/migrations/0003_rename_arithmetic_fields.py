# Generated by Django 4.1.3 on 2022-11-06 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_arithmetic_delete_fields'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Arithmetic',
            new_name='Fields',
        ),
    ]