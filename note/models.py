import uuid

from django.db import models
from category.models import Categories


class Notes(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, blank=True, default=uuid.uuid1, unique=True)
    text = models.TextField(max_length=500, blank=True)
    password = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='notes')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
