from django.db import models

# Create your models here.
class Note(models.Model):
	body = models.TextField(null=True, blank=True)
	# auto_now takes the system time automatically
	updated = models.DateTimeField(auto_now=True)
	# auto_now_add inserts time at the time creation only
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.body[0:50]
	