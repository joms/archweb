# Generated by Django 2.1.4 on 2018-12-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releng', '0001_squashed_0005_auto_20180616_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='last_modified',
            field=models.DateTimeField(editable=False),
        ),
    ]