# Generated by Django 4.1.3 on 2022-11-21 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("project_first_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ownership",
            name="id_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner_ownership",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
