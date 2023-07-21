from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)