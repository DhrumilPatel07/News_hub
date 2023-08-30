from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.conf import settings
from django.contrib.sessions.models import Session

# Create your models here.
from django.utils.datetime_safe import date


class Employee(models.Model):
    eid     = models.CharField(max_length=20)
    ename   = models.CharField(max_length=100)
    econtact = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"

class Employees(models.Model):
    eid     = models.CharField(max_length=20)
    ename   = models.CharField(max_length=100)
    email = models.EmailField()
    econtact = models.CharField(max_length=15)

    class Meta:
        db_table = "employees"

class Addusernews(models.Model):
    CATEGORY_CHOICE = (
        ('National', 'National'),
        ('Politics', 'Politics'),
        ('Automobile', 'Automobile'),
        ('Business', 'Business'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Hatke', 'Hatke'),
        ('Health', 'Health'),
        ('International', 'International'),
        ('Miscellaneous', 'Miscellaneous'),
        ('Science', 'Science'),
        ('sports', 'sports'),
        ('Startup', 'Startup'),
        ('Technology', 'Technology'),
        ('World', 'World'),
    )




    user = models.ForeignKey(User, on_delete=models.CASCADE)
    newstitle = models.CharField(max_length=20)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICE, default='-----')
    news = models.TextField()
    city = models.CharField(max_length=300, default='')
    publish_type = models.BooleanField(default=True)
    publish_date = models.DateField(default=datetime.today, null=True)
    # publish_date = models.DateField(default=datetime.date.today)
    # createdTime = models.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    # widgets = {
    #     'relatednews' : models.CharField(required=True, widget=models.CheckboxSelectMultiple, choices=NEWS_CHOICE)
    # }





