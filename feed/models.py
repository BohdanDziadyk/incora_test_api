from django.db import models


# Create your models here.

class Feed(models.Model):
    class Meta:
        db_table = 'feed'

    title = models.CharField(max_length=100, default='')
    url = models.URLField(max_length=255, default='')
