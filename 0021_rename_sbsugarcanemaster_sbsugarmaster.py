# Generated by Django 5.0.3 on 2024-04-17 07:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("nursery", "0020_labourmaster"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SbsugarcaneMaster",
            new_name="SbsugarMaster",
        ),
    ]