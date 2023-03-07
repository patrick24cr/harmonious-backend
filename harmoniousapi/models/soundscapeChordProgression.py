from django.db import models
from .soundscape import Soundscape
from .chordProgression import ChordProgression

class SoundscapeChordProgression(models.Model):
    
    soundscape = models.ForeignKey(Soundscape, on_delete=models.CASCADE)
    chordProgression = models.ForeignKey(ChordProgression, on_delete=models.CASCADE)
