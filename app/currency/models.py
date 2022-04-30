from django.db import models


class ContactUs(models.Model):
    email_from = models.CharField(max_length=50)
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=3000)


class Rate(models.Model):
    type = models.CharField(max_length=3)
    source = models.CharField(max_length=50)
    created = models.DateTimeField()
    buy = models.DecimalField(max_digits=10, decimal_places=2)
    sale = models.DecimalField(max_digits=10, decimal_places=2)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=25)
