# Generated by Django 2.2.7 on 2020-10-25 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parrot_control', '0004_parrotcommand_voice_relative_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parrotcommand',
            name='voice_file',
        ),
    ]
