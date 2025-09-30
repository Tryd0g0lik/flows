"""
models_views/type.py
"""

from django.db import models

# Create your models_views here.
from django.core import validators
from django.utils.translation import gettext_lazy as _

from flow.models import InitialModel
from flow.models_views.categories import CategoryModel


# from flow.models_views.categories import CategorySubcategory


class TypeFlowModel(InitialModel):
    name = models.CharField(
        max_length=50,
        help_text="50 is MAX length of name.",
        verbose_name=_("Name of type"),
        validators=[
            validators.RegexValidator(
                regex="(^[A-Za-z][A-Za-z0-9_]{1,50}$)",
                message="Check valid a name.",
            ),
            validators.MaxLengthValidator(50),
        ],
    )
    # category_id = models.ForeignKey(
    #     CategorySubcategory,
    #     on_delete=models.CASCADE,
    #     related_name="categoryname",
    #     verbose_name=_("Category"),
    # )
    category_id = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, related_name="Category"
    )
    # subcategory_id = models.ForeignKey(
    #     "SubCategory", on_delete=models.CASCADE, related_name="Category"
    # )

    class Meta:
        verbose_name = _("Type")
        verbose_name_plural = _("Types")
        unique_together = ["name", "category_id"]
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.slug = self.slug.lower()
        super().save(*args, **kwargs)
