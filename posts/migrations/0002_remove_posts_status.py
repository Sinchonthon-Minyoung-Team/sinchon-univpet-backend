# Generated by Django 4.2.4 on 2023-08-25 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='status',
        ),
    ]
