# Generated by Django 4.2.5 on 2024-10-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0003_task_year_in_school"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="year_in_school",
        ),
        migrations.AddField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[("todo", "To do"), ("in_p", "In process"), ("done", "Done")],
                default="todo",
                max_length=4,
            ),
        ),
    ]