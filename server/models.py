from django.contrib.gis.db import models
import random


class Team(models.Model):
	name = models.CharField(max_length=100)
	#TODO: add fields like points, money, etc...
	def __unicode__(self):
        return self.name




class User(models.Model):
	nickname = models.CharField(max_length=100)
	password = models.CharField(max_length=128)
	#TODO: add fields like points, money, etc...
	team = models.ForeignKey(Team)
	def __unicode__(self):
        return self.nickname

	def set_password(self, raw_password):
		algo = 'sha1'
		salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
		hsh = get_hexdigest(algo, salt, raw_password)
		self.password = '%s$%s$%s' % (algo, salt, hsh)


class Venue(models.Model):
	name = models.CharField(max_length=100)
	geometry = models.PointField()
	objects = models.GeoManager()
	#TODO:  manage category and owning team
	def __unicode__(self):
        return self.name
