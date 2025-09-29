"""
models_views/subcategories.py
"""

from django.db import models

# Create your models_views here.
from django.core import validators
from django.utils.translation import gettext_lazy as _

from flow.models import InitialModel
from flow.models_views.categories import CategoryModel
from project.settings import SUBCATEGORY


class SubCategory(InitialModel):
    """
    This is model of sub categories
    """

    category_id = models.ForeignKey(
        CategoryModel,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name=_("Category"),
    )
    name = models.CharField(
        max_length=100,
        choices=SUBCATEGORY,
        default=SUBCATEGORY[0][0],
        help_text="100 is MAX length of sub-category name.",
        verbose_name=_("Subcategory name"),
        unique=True,
        validators=[
            validators.RegexValidator(
                regex="(^[A-Za-z][A-Za-z0-9_]{1,100}$)",
                message="Check valid the category name.",
            ),
            validators.MaxLengthValidator(100),
        ],
    )

    class Meta:
        verbose_name = _("Subcategory")
        verbose_name_plural = _("Subcategories")
        unique_together = ["category", "name"]
        ordering = ["category", "name"]

    def __str__(self):
        return f"{self.category_id.name} - {self.name}"

    def get_absolute_url(self):
        return f"/category/{self.category.slug}/{self.slug}/"
