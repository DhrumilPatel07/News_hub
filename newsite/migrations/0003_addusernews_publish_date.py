# Generated by Django 4.0.6 on 2023-01-30 11:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsite', '0002_alter_addusernews_publish_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='addusernews',
            name='publish_date',
            field=models.DateField(default=datetime.datetime.today, null=True),
        ),
    ]
