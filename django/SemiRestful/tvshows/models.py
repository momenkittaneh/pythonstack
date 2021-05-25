from django.db import models

class show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date= models.DateField()
    desc = models.TextField()

