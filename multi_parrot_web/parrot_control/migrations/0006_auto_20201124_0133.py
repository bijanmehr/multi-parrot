# Generated by Django 2.2.7 on 2020-11-24 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parrot_control', '0005_remove_parrotcommand_voice_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voice_path_prefix', models.CharField(default='./', max_length=256)),
                ('voice_path_postfix', models.CharField(default='.wav', max_length=256)),
            ],
        ),
        migrations.RenameField(
            model_name='parrotcommand',
            old_name='voice_relative_path',
            new_name='voice_file_name',
        ),
    ]
