from django.db import models

# Create your models here.
class Music(models.Model):

    class Meta:
        db_table = "music"