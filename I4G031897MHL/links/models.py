from multiprocessing import managers
from django.contrib.auth import get_user_model
from django.db import models

from .managers import ActiveLinkManager
#from DjangoQueryset.I4G031897MHL.links.managers import ActiveLinkManager

# Create your models here.
class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank=True, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()