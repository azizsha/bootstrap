from django.db import models

class  bloggs(models.Model):
    title = models.CharField(max_length = 120)
    post = models.TextField()
    a = models.TextField()
    date = models.DateTimeField()
    opisanie = models.CharField(max_length = 120)
