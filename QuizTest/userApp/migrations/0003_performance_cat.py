# Generated by Django 4.0.4 on 2022-06-18 13:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_category_description'),
        ('userApp', '0002_performance'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.category'),
            preserve_default=False,
        ),
    ]