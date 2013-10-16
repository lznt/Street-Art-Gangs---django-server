from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, blank=True, null=True)
    time_checkin = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ('-time_checkin',)
        get_latest_by = 'time_checkin'

    def __unicode__(self):
        return self.name
