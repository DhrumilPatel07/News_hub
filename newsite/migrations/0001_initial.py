# Generated by Django 4.0.6 on 2022-09-24 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=20)),
                ('ename', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Addusernews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstitle', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('National', 'National'), ('Politics', 'Politics'), ('Automobile', 'Automobile'), ('Business', 'Business'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Hatke', 'Hatke'), ('Health', 'Health'), ('International', 'International'), ('Miscellaneous', 'Miscellaneous'), ('Science', 'Science'), ('sports', 'sports'), ('Startup', 'Startup'), ('Technology', 'Technology'), ('World', 'World')], default='-----', max_length=100)),
                ('news', models.TextField()),
                ('city', models.CharField(default='', max_length=300)),
                ('publish_type', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_news',
            },
        ),
    ]
