# Generated by Django 4.2.13 on 2024-06-18 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie_management", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="director",
        ),
        migrations.AlterField(
            model_name="movie",
            name="name",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="movie",
            name="production_year",
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name="Director",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie_management.artist",
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie_management.movie",
                    ),
                ),
            ],
            options={
                "unique_together": {("movie", "artist")},
            },
        ),
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie_management.artist",
                    ),
                ),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="movie_management.movie",
                    ),
                ),
            ],
            options={
                "unique_together": {("movie", "artist")},
            },
        ),
    ]
