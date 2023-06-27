from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=6)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")

@receiver(post_save, sender=Record)
def record_created(sender, instance, created, *args, **kwargs):
	if created:
		print("Record created successfully!", instance.id)
	else:
		print("Record created unsuccessfully", instance.id)
	


