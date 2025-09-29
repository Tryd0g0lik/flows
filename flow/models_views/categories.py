"""
models_views/categories.py
"""

from django.db import models

from django.core import validators
from django.utils.translation import gettext_lazy as _
from flow.models import InitialModel
from project.settings import CATEGORY


class CategoryModel(InitialModel):
    """
    This is model of categories
    TODO: добавить привязку подкатегории
    """

    name = models.CharField(
        max_length=50,
        choices=CATEGORY,
        default=CATEGORY[0][0],
        help_text="50 is MAX length of category name.",
        verbose_name=_("Category name"),
        unique=True,
        validators=[
            validators.RegexValidator(
                regex="(^[A-Za-z][A-Za-z0-9_]{1,50}$)",
                message="Check valid the category name.",
            ),
            validators.MaxLengthValidator(50),
        ],
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        unique_together = ["name"]
        ordering = ["name"]

    def __str__(self):
        return f"{self.type_id.name} - {self.name}"

    def get_absolute_url(self):
        return f"/category/{self.slug}/"
