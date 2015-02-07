from django.db import models
from django.conf import settings
from django.template.defaultfilters import date as _date
from django.utils import timezone

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	text = models.CharField(max_length=240)
	creation = models.DateTimeField(auto_now_add=True)

	def time(self):
		date = _date(timezone.localtime(self.creation),"H:i:s")
		return date