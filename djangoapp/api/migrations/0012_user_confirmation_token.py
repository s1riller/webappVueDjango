# Generated by Django 4.2.7 on 2023-11-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_trashbin_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmation_token',
            field=models.CharField(blank=True, max_length=30, verbose_name='confirmation_token'),
        ),
    ]
