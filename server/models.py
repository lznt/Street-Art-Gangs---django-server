from django.contrib.gis.db import models
from django.contrib.auth.models import Group, User


class Gang (models.Model):
    #TODO: add fields like points, money, etc...
    group = models.OneToOneField(Group, primary_key=True)

    def __unicode__(self):
        return  u"%s" % (self.group.name)





class Gangster(models.Model):

    #TODO: add fields like points, money, etc...
    user = models.OneToOneField(User, primary_key=True)
    gang = models.ForeignKey('Gang', related_name = 'gang')

    def __unicode__(self):
        return  u"%s, %s" % (self.user.username, self.gang.group.name)



class Venue(models.Model):

    #TODO:  manage category and owning team
    name = models.CharField(max_length=100)
    geometry = models.PointField()
    objects = models.GeoManager()
    owner = models.ForeignKey('Gang', related_name = 'owner')
    def __unicode__(self):
        return self.name
