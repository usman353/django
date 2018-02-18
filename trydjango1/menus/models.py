from django.db import models
from django.conf import settings
# Create your models here
from restaurants.models import RestaurantLocation


class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(RestaurantLocation, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='separate_by_commas')
    excludes = models.TextField(blank=True, null=True, help_text='separate_by_commas')
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-updated', '-timestamp']  # ordering by reverse updated meaning latest updated item top

    def get_contents(self):
        return self.contents.split(',')

    def get_excludes():
        return self.excludes.split(',')
