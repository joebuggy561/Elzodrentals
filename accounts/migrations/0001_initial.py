# Generated by Django 4.2.4 on 2023-08-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Register",
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
                ("name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=100, unique=True)),
                ("phone_number", models.CharField(max_length=50)),
                ("Country", models.CharField(max_length=50)),
            ],
        ),
    ]
