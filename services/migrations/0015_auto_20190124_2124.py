# Generated by Django 2.1 on 2019-01-25 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_servicepicturemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicetransactionmodel',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='servicetransactionmodel',
            name='service',
        ),
        migrations.AlterField(
            model_name='servicemodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ServiceTransactionModel',
        ),
    ]