# Generated by Django 4.2.7 on 2023-12-05 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0005_alter_survey_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='creator',
            new_name='author',
        ),
    ]