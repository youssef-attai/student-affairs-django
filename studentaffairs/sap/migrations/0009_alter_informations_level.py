# Generated by Django 3.2.13 on 2022-05-17 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap', '0008_auto_20220517_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informations',
            name='level',
            field=models.CharField(default='', max_length=500),
        ),
    ]
