from django.db import models

class History(models.Model):
    word = models.CharField("Word", max_length=100)
    vowels = models.IntegerField("Vowels", default=0)
    length = models.IntegerField("Length", default=0)
