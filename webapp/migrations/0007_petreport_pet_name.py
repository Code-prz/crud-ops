# Generated by Django 5.1.2 on 2025-01-09 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_petreport_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='petreport',
            name='pet_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]