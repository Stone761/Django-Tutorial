from django.db import models
from django.contrib.contenttypes.models import ContentType

class Name(models.Model):
    name_text = models.CharField(max_length=200)
    time_played = models.CharField(max_length=5)

class Rating(models.Model):
    name = models.ForeignKey(Name, null = True, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default = 1) 