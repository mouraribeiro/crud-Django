# Generated by Django 4.1.4 on 2022-12-18 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurantes", "0007_voto_hora_alter_voto_data"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="voto",
            name="hora",
        ),
    ]
