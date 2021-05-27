from django.db import models
class ShowManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 3:
            errors["title"] = "title  should be at least  2 characters"
        if len(postData['network']) < 5:
            errors["network"] = "network should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "description should be at least 5 characters"
        return errors

class show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date= models.DateField()
    desc = models.TextField()
    objects=ShowManager()

