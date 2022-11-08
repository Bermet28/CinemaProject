# Generated by Django 4.1.2 on 2022-11-08 05:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('post', 'owner')},
        ),
    ]