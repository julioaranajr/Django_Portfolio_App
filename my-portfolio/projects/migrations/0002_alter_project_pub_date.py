# Generated by Django 5.1.1 on 2024-09-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="pub_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="date published"
            ),
        ),
    ]
