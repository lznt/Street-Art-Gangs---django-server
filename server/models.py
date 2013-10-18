from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    tagsCreated = models.IntegerField()
    tagsDeleted = models.IntegerField()
    money = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return self.user.username


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])



class Venue(models.Model):
    CATEGORY_CHOICES = (
        ('Outdoors', 'Great Outdoors'),
        ('Nightlife', 'Nightlife Spots'),
        ('Aerts', 'Arts & Entertainment'),
        ('Education', 'Education'),
        ('Food', 'Food'),
        ('Other', 'Other Places'),
        ('Shop', 'Shops & Services'),
        ('Travel', 'Travel & Transport'),
    )
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, blank=True, null=True)
    latestEditTimestamp = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES)



    class Meta:
        ordering = ('-latestEditTimestamp',)
        get_latest_by = 'latestEditTimestamp'

    def __unicode__(self):
        return self.name
