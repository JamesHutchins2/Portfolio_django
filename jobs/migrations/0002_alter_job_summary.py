# Generated by Django 4.0.2 on 2022-02-25 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=500),
        ),
    ]
