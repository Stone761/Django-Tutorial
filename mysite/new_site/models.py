from django.db import models
from django.contrib.contenttypes.models import ContentType

class Name(models.Model):
    ## A model in django takes data and saves it to a database (help users do less work to properly save data) 
    ## name_text is just a text box asking the user to imput their name.
    name_text = models.CharField(max_length=200)
    time_played = models.CharField(max_length=5)

class Rating(models.Model):
    name = models.ForeignKey(Name, null = True, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default = 1) 

## A object in python has Atributes (Data) and Methods (Functions)
## A Class is a generalization of the type that an object is