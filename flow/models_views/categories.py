"""
models_views/categories.py
"""

from django.db import models

from django.core import validators
from django.utils.translation import gettext_lazy as _

from flow.models import InitialModel
from flow.models_views.subcategories import SubCategory


class CategoryModel(InitialModel):
    """
    This is model of categories
    TODO Модель SUB-Категория имеет колонку 'active' По умолчанию False.
        Заполняя  категорю, выбираем sub-категории. При сохранении, в SUB категории
        актиировая колонку 'active' из выбраныый позиций
    """

    slug = models.SlugField(unique=True, help_text=_("Unique identifier for URLs"))
    name = models.CharField(
        max_length=50,
        help_text="50 is MAX length of category name.",
        verbose_name=_("Category name"),
        validators=[
            validators.RegexValidator(
                regex="(^[A-Za-z][A-Za-z0-9_]{1,50}$)",
                message="Check valid the sub-category name.",
            ),
            validators.MaxLengthValidator(50),
        ],
    )
    subcategories = models.ManyToManyField(
        SubCategory, related_name="categories", verbose_name="categories"
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        unique_together = [
            "name",
        ]
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/category/{self.slug}/"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.slug = self.slug.lower()
        super().save(*args, **kwargs)
