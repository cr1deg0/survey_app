# Generated by Django 4.2.7 on 2023-12-10 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0009_alter_option_question_alter_question_survey_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='survey',
            options={'ordering': ['-created'], 'permissions': (('view_own_survey', 'Can view own survey'), ('edit_own_survey', 'Can edit own survey'))},
        ),
    ]
