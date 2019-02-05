# Generated by Django 2.1 on 2019-02-03 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20190202_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrymodel',
            name='buyer_notes',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='entrymodel',
            name='days_remaining',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entrymodel',
            name='seller_notes',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]