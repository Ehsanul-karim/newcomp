# Generated by Django 4.2.6 on 2023-11-12 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_relation_witnessinfo_relationwithvictim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case_fir',
            old_name='district',
            new_name='occuranced_district',
        ),
        migrations.RenameField(
            model_name='case_fir',
            old_name='division',
            new_name='occuranced_division',
        ),
        migrations.RenameField(
            model_name='case_fir',
            old_name='upazila',
            new_name='occuranced_upazila',
        ),
    ]
