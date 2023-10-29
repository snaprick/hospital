# Generated by Django 4.2.6 on 2023-10-29 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_doctor_patient_service_specialization_visit_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="visit",
            name="visit_date_time",
        ),
        migrations.AlterField(
            model_name="visit",
            name="doctor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="visits",
                to="api.doctor",
            ),
        ),
        migrations.AlterField(
            model_name="visit",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="visits",
                to="api.patient",
            ),
        ),
        migrations.CreateModel(
            name="Schedule",
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
                ("timestamp_start", models.DateTimeField()),
                ("timestamp_end", models.DateTimeField()),
                (
                    "doctor",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="schedules",
                        to="api.doctor",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="schedules",
                        to="api.patient",
                    ),
                ),
                (
                    "visit",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="schedules",
                        to="api.visit",
                    ),
                ),
            ],
        ),
    ]
