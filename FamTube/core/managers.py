from django.db import models
from django.db.models import Q


class FilterManager(models.Manager):
	def by_title(self, title):
		return self.filter(title__icontains=title)

	def by_description(self, description):
		return self.filter(description__icontains=description)

	def get_all(self):
		return self.all().order_by('-published_on')
