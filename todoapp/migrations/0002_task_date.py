# Generated by Django 3.2.5 on 2021-07-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
    ]