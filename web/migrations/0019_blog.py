# Generated by Django 3.2.6 on 2023-01-29 12:50

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_manhwa_alternate_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=500, unique=True)),
                ('content', mdeditor.fields.MDTextField()),
            ],
        ),
    ]
