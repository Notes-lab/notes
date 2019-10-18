import uuid

from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, blank=True, default=uuid.uuid1, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
