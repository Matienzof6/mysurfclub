from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    imagen = models.ImageField(upload_to='img', null=True, blank=True)

    class Meta:
        verbose_name='Member'
        verbose_name_plural='Members'
