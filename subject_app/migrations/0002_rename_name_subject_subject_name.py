# Generated by Django 5.0.3 on 2024-03-24 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='subject_name',
        ),
    ]
