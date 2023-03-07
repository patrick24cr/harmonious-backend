from django.db import models

class Chord(models.Model):

    name = models.CharField(max_length=20)
    rootNote = models.CharField(max_length=20)
    quality = models.CharField(max_length=20)
    texture1filepath = models.CharField(max_length=200)
    texture2filepath = models.CharField(max_length=200)
    texture3filepath = models.CharField(max_length=200)
