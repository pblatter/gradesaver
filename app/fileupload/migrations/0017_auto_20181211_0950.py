# Generated by Django 2.0.5 on 2018-12-11 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fileupload', '0016_auto_20181211_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test_files',
            name='user',
        ),
        migrations.AddField(
            model_name='test_files',
            name='user',
            field=models.ForeignKey(default=-1.0, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
