# Generated by Django 2.0.5 on 2018-11-17 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0005_auto_20181116_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice_test',
            name='status',
            field=models.IntegerField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')]),
        ),
    ]
