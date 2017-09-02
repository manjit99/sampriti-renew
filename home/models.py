from django.db import models
import datetime

# Create your models here.

class NormalPost(models.Model):
    Title     = models.CharField(max_length=500, null=False, blank=False)
    Timestamp = models.DateTimeField(blank=False, default=datetime.datetime.now)
    Updated   = models.DateTimeField(auto_now = True)
    About     = models.TextField(blank=False)
    Readmore  = models.URLField(null=True, blank=True, max_length=5000)
    SecondTitle = models.CharField(max_length=8,default='readmore', null= True, blank= True)

    def __unicode__(self):
        return self.Title

    def __str__(self):
        return self.Title

    class Meta:
        ordering = ["-Timestamp", "-Updated"]
