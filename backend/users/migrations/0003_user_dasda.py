# Generated by Django 2.2.28 on 2022-08-24 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220823_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dasda',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
