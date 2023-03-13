from django.db import models

# Create your models here.
# Form model with Image field to be uploaded.
class Sign(models.Model):
	gesture = models.ImageField(upload_to='',blank=False)