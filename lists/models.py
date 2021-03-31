# Django
from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    user = models.ForeignKey(
        User,
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

    created = models.DateTimeField(
        auto_now_add=True
    )

    modified = models.DateTimeField(
        auto_now=True
    )
