# Generated by Django 5.0.3 on 2024-03-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nursery", "0016_rename_nurser_date_pbledgermaster_nursery_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="addpureMaster",
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
                ("item", models.CharField(max_length=200, null=True)),
                ("price", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="PbledgerMaster",
        ),
    ]