# Generated by Django 3.0.2 on 2020-01-27 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0018_auto_20200127_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='centrelink',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='healthcare_card',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='income_bracket',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='special_consideration',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='special_consideration_note',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='studying_fulltime',
        ),
    ]