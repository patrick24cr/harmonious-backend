from django.db import models
from .chord import Chord

class ChordProgression(models.Model):

    name = models.CharField(max_length=20)
    firstChord = models.ForeignKey(Chord, on_delete=models.CASCADE, related_name='firstChord')
    secondChord = models.ForeignKey(Chord, on_delete=models.CASCADE, related_name='secondChord')
    thirdChord = models.ForeignKey(Chord, on_delete=models.CASCADE, related_name='thirdChord')
    fourthChord = models.ForeignKey(Chord, on_delete=models.CASCADE, related_name='fourthChord')
