from django.db import models
from django.utils import timezone

# Create your models here.
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/images/')
    song = models.FileField(upload_to='static/audio/')
    first_prompt=models.FloatField(default=0)
   

    def __str__(self):
        return str(self.song_id)

class add(models.Model):
    prompt_id = models.ForeignKey('Song',on_delete=models.CASCADE)
    prompt_no=models.IntegerField(default=1)
    yesurl = models.FileField(upload_to='static/audio/')
    nourl = models.FileField(upload_to='static/audio/')
    prompturl = models.FileField(upload_to='static/audio/')
    next_prompt=models.FloatField (default=0)
    previous_prompt=models.FloatField (default=0)
    no_action=models.FloatField (default=0)


class detail(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)