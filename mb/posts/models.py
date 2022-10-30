from django.db import models

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50] #this will return the first 50 characters of the text field


