from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    gang = models.ForeignKey('Gang', related_name='gangsters')
    tagsCreated = models.IntegerField()
    tagsDeleted = models.IntegerField()
    money = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

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
    user = models.ForeignKey(User, blank=True, null=True)
    latestEditTimestamp = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)



    class Meta:
        ordering = ('-latestEditTimestamp',)
        get_latest_by = 'latestEditTimestamp'

    def __unicode__(self):
        return self.name
