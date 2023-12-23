from django.db import models

class Home(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)

