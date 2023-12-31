# Generated by Django 4.2.7 on 2023-11-18 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0042_case_fir_occurance_time_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CriminalProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("criminal_name", models.CharField(max_length=255, null=True)),
                ("criminal_nid", models.CharField(max_length=255, null=True)),
                ("criminal_DOB", models.DateField(null=True)),
                ("criminal_email", models.CharField(max_length=255, null=True)),
                ("criminal_phone", models.CharField(max_length=255, null=True)),
                ("criminal_division", models.CharField(max_length=255, null=True)),
                ("criminal_district", models.CharField(max_length=255, null=True)),
                ("criminal_thana", models.CharField(max_length=255, null=True)),
                ("criminal_crimes", models.CharField(max_length=255, null=True)),
                ("criminal_arrest_date", models.DateField(null=True)),
                ("criminal_gender", models.CharField(max_length=255, null=True)),
                ("criminal_hair_color", models.CharField(max_length=255, null=True)),
                ("criminal_skin_tone", models.CharField(max_length=255, null=True)),
                ("criminal_hair_style", models.CharField(max_length=255, null=True)),
                ("criminal_hair_length", models.CharField(max_length=255, null=True)),
                ("criminal_age", models.CharField(max_length=255, null=True)),
                ("criminal_face_shape", models.CharField(max_length=255, null=True)),
                ("criminal_facial_hair", models.CharField(max_length=255, null=True)),
                ("criminal_height", models.CharField(max_length=255, null=True)),
                ("criminal_weight", models.CharField(max_length=255, null=True)),
                ("criminal_marks", models.CharField(max_length=255, null=True)),
                (
                    "criminal_fir_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.case_fir",
                    ),
                ),
            ],
        ),
    ]
