# Generated by Django 3.2.6 on 2021-08-15 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0011_alter_manhwalist_manhwas"),
    ]

    operations = [
        migrations.AddField(
            model_name="manhwalist",
            name="description",
            field=models.TextField(default="dfjdkfjdf"),
            preserve_default=False,
        ),
    ]