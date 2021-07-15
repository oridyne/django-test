import datetime

from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Flower(models.Model):
    name = models.CharField(max_length=100)
    species_name = models.CharField(max_length=300)
    family_name = models.CharField(max_length=300)
    description = models.TextField()
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
