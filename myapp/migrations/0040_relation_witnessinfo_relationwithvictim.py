# Generated by Django 4.2.6 on 2023-11-12 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_remove_witnessinfo_relationwithvictim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOfRelations', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='witnessinfo',
            name='relationWithVictim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.relation'),
        ),
    ]
