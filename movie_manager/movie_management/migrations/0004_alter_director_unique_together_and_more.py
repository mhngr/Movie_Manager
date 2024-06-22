# Generated by Django 4.2.13 on 2024-06-21 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("movie_management", "0003_apicall"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="director",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="director",
            name="artist",
        ),
        migrations.RemoveField(
            model_name="director",
            name="movie",
        ),
        migrations.AlterModelOptions(
            name="apicall",
            options={},
        ),
        migrations.RemoveField(
            model_name="apicall",
            name="timestamp",
        ),
        migrations.AddField(
            model_name="movie",
            name="actor",
            field=models.ManyToManyField(
                related_name="director_movies", to="movie_management.artist"
            ),
        ),
        migrations.AddField(
            model_name="movie",
            name="director",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="actor_movies",
                to="movie_management.artist",
            ),
        ),
        migrations.DeleteModel(
            name="Actor",
        ),
        migrations.DeleteModel(
            name="Director",
        ),
    ]
