from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    time_checkin = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        ordering = ('-time_checkin',)
        get_latest_by = 'time_checkin'

    def __unicode__(self):
        return self.name
