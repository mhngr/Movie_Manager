# Generated by Django 4.2.13 on 2024-06-22 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_management", "0005_artist_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="role",
            field=models.CharField(
                choices=[(0, "actor"), (1, "director")], max_length=20, null=True
            ),
        ),
    ]
