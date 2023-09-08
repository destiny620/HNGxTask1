from django.db import models
import datetime
# from datetime import datetime
import pytz


# Create your models here.

def get_date():
    today = datetime.datetime.now()
    return today - datetime.timedelta(today.weekday())

class Track(models.Model):
    slack = models.CharField(max_length=50, default='')
    day = models.DateField(datetime.datetime.now().strftime("%A"))
    time = models.DateTimeField(datetime.datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    track = models.CharField(max_length=50, default='')
    furl = models.CharField(max_length=200)
    repo = models.CharField(max_length=200)
    status = models.IntegerField()

    def __str__(self):
        return self.slack + " " + self.track
    

 
