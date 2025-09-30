"""
models_views/subcategories.py
"""

from django.db import models

# Create your models_views here.
from django.core import validators
from django.utils.translation import gettext_lazy as _

from flow.models import InitialModel


# from flow.models_views.categories import CategoryModel
# from project.settings import SUBCATEGORY


class SubCategory(InitialModel):
    """
    This is model of sub categories
    """

    name = models.CharField(
        max_length=100,
        # choices=SUBCATEGORY,
        # default=SUBCATEGORY[0][0],
        help_text="100 is MAX length of sub-category name.",
        verbose_name=_("Subcategory name"),
        unique=True,
        validators=[
            validators.RegexValidator(
                regex="(^[A-Za-z][A-Za-z0-9_]{1,100}$)",
                message="Check valid the sub-category name.",
            ),
            validators.MaxLengthValidator(100),
        ],
    )

    class Meta:
        verbose_name = _("Subcategory")
        verbose_name_plural = _("Subcategories")
        unique_together = ["name"]
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/subcategory/{self.slug}/"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.slug = self.slug.lower()
        super().save(*args, **kwargs)
