# Generated by Django 4.0.4 on 2022-06-18 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_category_description'),
        ('userApp', '0005_remove_performance_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.category'),
        ),
    ]
