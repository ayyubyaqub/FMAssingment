# Generated by Django 5.0 on 2023-12-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order',
            name='po_delivered_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
