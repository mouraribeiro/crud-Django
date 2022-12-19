# Generated by Django 4.1.4 on 2022-12-18 17:28

from django.db import migrations, models
import django.db.models.deletion
import restaurantes.models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurantes", "0008_remove_voto_hora"),
    ]

    operations = [
        migrations.CreateModel(
            name="Escolha",
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
                ("escolha", models.CharField(max_length=255)),
                (
                    "restaurante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurantes.restaurante",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vote",
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
                    "choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurantes.escolha",
                    ),
                ),
                (
                    "restaurante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurantes.restaurante",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item",
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
                    "option",
                    models.CharField(
                        max_length=250, verbose_name=restaurantes.models.Restaurante
                    ),
                ),
                ("position", models.SmallIntegerField(default="0")),
                (
                    "voto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurantes.restaurante",
                    ),
                ),
            ],
        ),
    ]
