from django.db import models
from .user import User
from .melodyTexture import MelodyTexture

class Soundscape(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    chordTexture = models.IntegerField()
    melodyNotes = models.CharField(max_length=50)
    melodyTexture = models.ForeignKey(MelodyTexture, on_delete=models.CASCADE)
