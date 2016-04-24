from django.db import models

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=20,unique=True)
    def __unicode__(self):
        return self.name
