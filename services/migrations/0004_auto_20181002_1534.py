# Generated by Django 2.1 on 2018-10-02 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20181001_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='services.CategoryModel'),
        ),
    ]