# Generated by Django 4.2.6 on 2023-11-10 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_case_fir'),
    ]

    operations = [
        migrations.CreateModel(
            name='witness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('witness_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.witnessinfo')),
            ],
        ),
        migrations.AlterField(
            model_name='case_fir',
            name='witness_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.witness'),
        ),
    ]
