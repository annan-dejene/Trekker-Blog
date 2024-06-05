# Generated by Django 5.0.6 on 2024-06-05 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_comment_created_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=255)),
                ("slug", models.SlugField()),
            ],
            options={
                "ordering": ["title"],
            },
        ),
    ]