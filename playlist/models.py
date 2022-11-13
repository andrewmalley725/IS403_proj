from django.db import models

# Create your models here.
class Songs(models.Model):
    SongName = models.CharField(max_length=30, null=False)
    Artist = models.CharField(max_length=20, null=False)
    Album = models.CharField(max_length=20, null=False)
    YearReleased = models.IntegerField(null=False)

    def __str__(self):
        return self.SongName
