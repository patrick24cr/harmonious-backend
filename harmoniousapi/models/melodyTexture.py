from django.db import models

class MelodyTexture(models.Model):

    name = models.CharField(max_length=20)
    synthSetting1 = models.IntegerField()
    synthSetting2 = models.IntegerField()
    synthSetting3 = models.IntegerField()
