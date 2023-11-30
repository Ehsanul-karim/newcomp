# Generated by Django 4.2.6 on 2023-11-08 10:30

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_adminprofile_varified'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicalStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criminal_id', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('hairColor', models.CharField(max_length=255)),
                ('skinTone', models.CharField(max_length=255)),
                ('hairStyle', models.CharField(max_length=255)),
                ('hairLength', models.CharField(max_length=255)),
                ('eyeColor', models.CharField(max_length=255)),
                ('faceShape', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('leftFacedImage', models.ImageField(upload_to=myapp.models.filepath)),
                ('FrontFacedImage', models.ImageField(upload_to=myapp.models.filepath)),
                ('RightFacedImage', models.ImageField(upload_to=myapp.models.filepath)),
            ],
        ),
    ]
