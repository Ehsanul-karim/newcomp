# Generated by Django 4.2.6 on 2023-12-01 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0049_remove_criminalprofile_criminal_fir_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criminalprofile',
            name='criminal_firs',
        ),
    ]