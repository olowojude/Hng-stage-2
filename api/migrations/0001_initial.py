# Generated by Django 4.1.3 on 2022-11-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.CharField(max_length=50)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
    ]