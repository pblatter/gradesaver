# Generated by Django 2.0.5 on 2018-11-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0010_test_files_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_files',
            name='Exam',
            field=models.FileField(upload_to=''),
        ),
    ]
