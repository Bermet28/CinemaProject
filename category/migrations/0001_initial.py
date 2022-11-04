# Generated by Django 4.1.2 on 2022-11-04 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, unique=True)),
                ('descriptions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('slug', models.SlugField(max_length=100)),
                ('title', models.SlugField(max_length=100, primary_key=True, serialize=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='genre', to='category.category')),
            ],
        ),
    ]
