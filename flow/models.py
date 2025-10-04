"""
models_views/categories.py
"""

from django.utils.translation import gettext_lazy as _

from django.db import models


class InitialModel(models.Model):
    """
    This is abstract model
    """

    slug = models.SlugField(unique=True, help_text=_("Unique identifier for URLs"))

    class Meta:
        abstract = True
