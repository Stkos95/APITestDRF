# Generated by Django 4.2.5 on 2023-10-04 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_alter_viewdetail_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewdetail',
            name='when_watched',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]