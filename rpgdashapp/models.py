from django.db import models
from django.db.models import Sum

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000, blank=True)

	def __unicode__(self):
        	return self.name
	

class Skill(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000, blank=True)
	category = models.ForeignKey(Category)

	def __unicode__(self):
        	return self.name

class Achievement(models.Model):
	skill = models.ForeignKey(Skill)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	completed = models.BooleanField(default=False)
	dateCompleted = models.DateField(null = True, blank=True)

	def __unicode__(self):
        	return self.name

class Metric(models.Model):
	skill = models.ForeignKey(Skill)
	name = models.CharField(max_length=200)

	def __unicode__(self):
        	return self.name

	def metricValue(self):
		toReturn = Activity.objects.filter(metric=self).aggregate(Sum('value'))[ 'value__sum' ]
		if toReturn == None:
			toReturn = 0
		return toReturn

class Activity(models.Model):
	metric = models.ForeignKey(Metric)
	description = models.CharField(max_length=1000, blank=True)
	value = models.FloatField()

	def __unicode__(self):
		toReturn = self.metric.name + " - " + str(self.value)
		if self.description <> "":
			toReturn += " (" + self.description + ")"
        	return toReturn

class Person(models.Model):
	name = models.CharField(max_length=200)
	birthday = models.DateField()
	image = models.ImageField(upload_to="personPictures")

	def __unicode__(self):
		return self.name
