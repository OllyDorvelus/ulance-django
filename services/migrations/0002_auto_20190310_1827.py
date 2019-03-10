# Generated by Django 2.1 on 2019-03-10 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='jobmodel',
            name='freelancer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]