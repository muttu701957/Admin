# Generated by Django 5.0.3 on 2024-03-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nursery", "0005_auto_20240310_2326"),
    ]

    operations = [
        migrations.CreateModel(
            name="customer",
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
                ("farmer_name", models.CharField(max_length=200, null=True)),
                ("address", models.CharField(max_length=200, null=True)),
                ("mobile_num", models.IntegerField(blank=True, null=True)),
                ("packet_no", models.IntegerField(blank=True, null=True)),
                ("packet_name", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="purchagemaster",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
