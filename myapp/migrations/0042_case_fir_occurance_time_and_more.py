# Generated by Django 4.2.7 on 2023-11-18 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0041_rename_district_case_fir_occuranced_district_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="case_fir",
            name="occurance_time",
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name="physicalstructure",
            name="dis_guis_mark",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="physicalstructure",
            name="dis_guis_mark_brief",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="victim_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="myapp.victiminfo",
            ),
        ),
        migrations.AlterField(
            model_name="physicalstructure",
            name="age",
            field=models.CharField(
                choices=[
                    ("MINOR", "Minor"),
                    ("YOUNG", "Young"),
                    ("ADULT", "Adult"),
                    ("AGED", "Aged"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="physicalstructure",
            name="height",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="physicalstructure",
            name="weight",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
