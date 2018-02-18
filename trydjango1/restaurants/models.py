from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from .validators import validate_categories
from django.urls import reverse

# Create your models here.

User = settings.AUTH_USER_MODEL


class RestaurantLocation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # klass instance.model_set.all()
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    categories = models.CharField(max_length=120, null=True, blank=True, validators=[validate_categories])
    timestamp = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)
    # my_date_field = models.DateTimeField(auto_now_add=False, auto_now=False)
    recommend = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):  # without this objects will have to be called with .name
        return self.name

    def get_absolute_url(self):
        return reverse('restaurants:detail', kwargs={'slug': self.slug}) # restaurants is the namespace while detail is name in app/urls.py

    @property
    def title(self):
        return self.name  # this property add the ability to get object.title and convert it into .name as object.title name is used in utils.py so this is for learning we can change in utils but this new.


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.categories = instance.categories.title()
    print('saving')
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
        print(instance.slug)


# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#     print('saved')
#     print(instance.timestamp)
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
#         instance.save()


pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)
