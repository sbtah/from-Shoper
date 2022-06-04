from django.db import models


class Tag(models.Model):
    """Model for Tag object. Used for grouping of products."""

    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"TAG:{self.id};{self.name}"
