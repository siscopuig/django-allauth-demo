# Generated by Django 2.2.5 on 2019-09-17 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190917_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_image',
            new_name='image',
        ),
    ]
