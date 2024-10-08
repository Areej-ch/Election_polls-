# Generated by Django 5.1.1 on 2024-09-27 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Poll",
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
                ("question", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="pollingstation",
            name="election",
        ),
        migrations.RemoveField(
            model_name="result",
            name="polling_station",
        ),
        migrations.CreateModel(
            name="Choice",
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
                ("choice_text", models.CharField(max_length=200)),
                ("votes", models.IntegerField(default=0)),
                (
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="polls.poll"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Election",
        ),
        migrations.DeleteModel(
            name="PollingStation",
        ),
        migrations.DeleteModel(
            name="Result",
        ),
    ]
