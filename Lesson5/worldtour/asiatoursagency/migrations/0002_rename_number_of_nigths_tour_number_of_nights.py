# Generated by Django 5.0.7 on 2024-08-05 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asiatoursagency', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='number_of_nigths',
            new_name='number_of_nights',
        ),
    ]
