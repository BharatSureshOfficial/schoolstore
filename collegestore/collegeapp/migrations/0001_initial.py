# Generated by Django 4.2.3 on 2023-07-28 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Course",
                "verbose_name_plural": "Courses",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Department",
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
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name": "Department",
                "verbose_name_plural": "Departments",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="FormData",
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
                ("name", models.CharField(max_length=100)),
                ("dob", models.DateField(blank=True, null=True)),
                ("age", models.PositiveIntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=10
                    ),
                ),
                ("phone_number", models.CharField(max_length=20)),
                ("mail_id", models.EmailField(max_length=254)),
                ("address", models.TextField()),
                ("purpose", models.CharField(max_length=50)),
                ("materials_provide", models.CharField(max_length=200)),
                (
                    "course",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="collegeapp.course",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="collegeapp.department",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="collegeapp.department"
            ),
        ),
    ]
