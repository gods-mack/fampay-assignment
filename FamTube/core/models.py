from django.db import models
from .managers import FilterManager

class FamVideo(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	published_on = models.DateTimeField(db_index=True)
	description = models.TextField()
	small_thumbnail = models.CharField(max_length=255, null=True, blank=True)
	medium_thumbnail = models.CharField(max_length=255, null=True, blank=True)
	large_thumbnail = models.CharField(max_length=255, null=True, blank=True)

	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	objects = FilterManager()

	def serializer(self):
		serialized_object = {}
		serialized_object['title'] = self.title
		serialized_object['description'] = self.description
		serialized_object['published_on'] = str(self.published_on)
		serialized_object['small_thumbnail'] = self.small_thumbnail
		serialized_object['medium_thumbnail'] = self.medium_thumbnail
		serialized_object['large_thumbnail'] = self.large_thumbnail
		return serialized_object


