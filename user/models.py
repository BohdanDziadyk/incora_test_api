from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'user'

    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
