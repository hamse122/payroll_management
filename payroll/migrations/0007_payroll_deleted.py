# Generated by Django 5.0.2 on 2024-05-15 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0006_remove_payroll_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
