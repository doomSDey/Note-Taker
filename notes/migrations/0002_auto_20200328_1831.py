# Generated by Django 3.0.4 on 2020-03-28 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color',
            field=models.CharField(default='yellow', max_length=120),
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='Note', max_length=120),
        ),
    ]
