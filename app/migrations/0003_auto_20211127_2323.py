# Generated by Django 3.2.8 on 2021-11-27 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211127_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photos',
            name='category',
        ),
        migrations.AddField(
            model_name='photos',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
