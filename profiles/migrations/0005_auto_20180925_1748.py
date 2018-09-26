# Generated by Django 2.1 on 2018-09-25 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0004_auto_20180924_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('skill_level', models.CharField(choices=[('BG', 'Beginner'), ('IT', 'Intermediate'), ('EX', 'Expert')], default='BG', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='skillmodel',
            name='skill_level',
        ),
        migrations.AddField(
            model_name='levelmodel',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.SkillModel'),
        ),
        migrations.AddField(
            model_name='levelmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
