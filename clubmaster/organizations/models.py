from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    """
    The model representation of an Organization.
    """
    identifier = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=30)
    website = models.URLField(blank=True)
    # logo = models.ImageField(blank=True)
    contact = models.EmailField()
    description = models.CharField(max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE)