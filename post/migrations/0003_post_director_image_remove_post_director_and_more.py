# Generated by Django 4.1.2 on 2022-11-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_rename_user_like_owner_alter_like_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='director_image',
            field=models.ImageField(null=True, upload_to='directors', verbose_name='director'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='director',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.AddField(
            model_name='post',
            name='director',
            field=models.CharField(max_length=100, null=True),
        ),
    ]