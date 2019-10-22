import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Categories(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, default=uuid.uuid1, unique=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
