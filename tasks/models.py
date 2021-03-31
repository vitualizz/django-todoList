# Django
from django.db import models

# Models
from lists.models import List


class Task(models.Model):
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    description = models.TextField(
        blank=True
    )

    completed = models.BooleanField(
        default=False
    )

    expired_at = models.DateTimeField(
        null=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    modified = models.DateTimeField(
        auto_now=True
    )

