"""
models_views/categories.py
"""

from django.db import models

# Create your models_views here.
from django.core import validators
from django.core import validators
from django.utils.translation import gettext_lazy as _


class InitialModel(models.Model):
    """
    This is abstract model
    """

    slug = models.SlugField(unique=True, help_text=_("Unique identifier for URLs"))

    class Meta:
        abstract = True
