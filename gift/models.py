from django.db import models

class item(models.Model):
    nav1 = models.CharField(max_length=20)
    nav2 = models.CharField(max_length=20)
    nav3 = models.CharField(max_length=20)
    nav4 = models.CharField(max_length=20)

# Create your models here.
