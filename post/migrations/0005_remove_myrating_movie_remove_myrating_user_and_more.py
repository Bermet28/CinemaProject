# Generated by Django 4.1.2 on 2022-11-09 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_myrating_mylist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myrating',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='myrating',
            name='user',
        ),
        migrations.DeleteModel(
            name='MyList',
        ),
        migrations.DeleteModel(
            name='Myrating',
        ),
    ]
