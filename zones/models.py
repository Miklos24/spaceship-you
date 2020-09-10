from django.db import models

# Create your models here.
class ZoneTimes(models.Model):
    # This field is temporary and will need to be replaced by a key to actual
    # users accounts.
    user = models.CharField(max_length=100)

    couch_alotted = models.IntegerField()
    couch_used = models.IntegerField()
    exercise_alotted = models.IntegerField()
    exercise_used = models.IntegerField()
    creative_allotted = models.IntegerField()
    creative_used = models.IntegerField()
    sleep_alotted = models.IntegerField()
    sleep_used = models.IntegerField()
