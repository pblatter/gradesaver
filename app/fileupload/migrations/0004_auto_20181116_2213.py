# Generated by Django 2.0.5 on 2018-11-16 22:13

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0003_choice_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice_test',
            name='relevance',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Unread'), (2, 'Read')], default=1, max_length=3),
        ),
        migrations.AlterField(
            model_name='choice_test',
            name='status',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Not relevant'), (2, 'Review'), (3, 'Maybe relevant'), (4, 'Relevant'), (5, 'Leading candidate')], max_length=9),
        ),
    ]
