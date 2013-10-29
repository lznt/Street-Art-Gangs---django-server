from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gang = models.ForeignKey('Gang', related_name='gangsters')
    tags_created = models.IntegerField(default=0)
    tags_deleted = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    last_action = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username

    def _acted_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(seconds=30) <= self.last_action <  now

    acted_recently = property(_acted_recently)


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Gang(models.Model):

    COLOR_CHOICES = (
        ('purple', 'Purple'),
        ('green', 'Green'),
        ('blue', 'Blue'),
    )

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100, choices=COLOR_CHOICES)


    def __unicode__(self):
        return self.name


class Venue(models.Model):
    CATEGORY_CHOICES = (
        ('Ou', 'Great Outdoors'),
        ('Ni', 'Nightlife Spots'),
        ('Ar', 'Arts & Entertainment'),
        ('Ed', 'Education'),
        ('Fo', 'Food'),
        ('Ot', 'Other Places'),
        ('Sh', 'Shops & Services'),
        ('Tr', 'Travel & Transport'),
    )
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, blank=True, null=True, related_name='venues')
    latestEditTimestamp = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)



    class Meta:
        ordering = ('-latestEditTimestamp',)
        get_latest_by = 'latestEditTimestamp'

    def __unicode__(self):
        return self.name
