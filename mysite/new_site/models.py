from django.db import models
# You're importing the models module from the django package.
from django.contrib.contenttypes.models import ContentType
# Content type is a way to dynamically associate models with each other. 


class Name(models.Model):
    ## A model in django takes data and saves it to a database (help users do less work to properly save data) 
    name_text = models.CharField(max_length=200)
    # name_text is a text box that allows users to imput their name.
    time_played = models.CharField(max_length=5)
    # time_played is also a text box for people to imput how long they've played.

class Rating(models.Model):
    # The rating class is a colection of data to assign a number rating to a user from up above
    name = models.ForeignKey(Name, null = True, on_delete=models.CASCADE)
    # This is giving you a selection of users to pick from to assign your rating to your name.
    ## ForeignKey essentially connects one model to another; ChatGPT says it creates a one-to-many relationship between models.
    ## on_delete=model.CASCADE means that if a name in this instance were to be deleted, it's rating would also bite the dust.
    user_rating = models.IntegerField(default = 1) 
    # The user_rating model is a box you can enter numbers in to signify your rating.



## A object in python has Atributes (Data) and Methods (Functions)
## A Class is a generalization of the type that an object is