# Generated by Django 3.1.4 on 2024-03-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchagemaster',
            name='purchage_date',
            field=models.DateField(null=True),
        ),
    ]