# Generated by Django 4.1.4 on 2022-12-17 13:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("restaurantes", "0004_remove_voto_pergunta_remove_voto_pub_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="voto",
            name="data",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="voto",
            name="user",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
