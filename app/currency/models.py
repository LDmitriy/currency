from django.db import models


class ContactUs(models.Model):
    email_from = models.CharField(max_length=50)
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=3000)
