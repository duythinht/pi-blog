from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
    text = models.CharField(max_length=160)
    link = models.CharField(max_length=200)
    detector = models.ForeignKey(User, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
