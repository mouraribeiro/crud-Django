# Generated by Django 4.1.4 on 2022-12-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurantes", "0006_voto_voto"),
    ]

    operations = [
        migrations.AddField(
            model_name="voto",
            name="hora",
            field=models.DateField(blank=True, null=True, verbose_name="data/hora"),
        ),
        migrations.AlterField(
            model_name="voto",
            name="data",
            field=models.DateTimeField(),
        ),
    ]
