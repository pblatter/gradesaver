# Generated by Django 2.0.5 on 2018-11-19 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0008_test_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_files',
            name='Lehrperson',
            field=models.CharField(max_length=50),
        ),
    ]