# Generated by Django 4.2 on 2023-04-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AccessApp", "0003_task_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="app_user",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
