from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gang = models.ForeignKey('Gang', related_name='gangsters')
    tagsCreated = models.IntegerField(default=0)
    tagsDeleted = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.user.username


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Gang(models.Model):
    name = models.CharField(max_length=100)

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
