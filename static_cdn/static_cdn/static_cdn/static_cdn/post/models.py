from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	image =models.FileField(upload_to=upload_location,null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	author = models.CharField(max_length= 20 ,null = True)
	email = models.EmailField(max_length = 100, null= True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post:detail", kwargs={"id": self.id})
