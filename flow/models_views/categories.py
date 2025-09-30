"""
models_views/categories.py
"""

from django.core.exceptions import ValidationError
from django.db import models

from django.core import validators
from django.db.models import Prefetch
from django.utils.translation import gettext_lazy as _

# from flow.admin import SubCategoryInLine
from flow.models import InitialModel
from flow.models_views.subcategories import SubCategory

# from project.settings import CATEGORY


class CategoryModel(InitialModel):
    """
    This is model of categories
    """

    slug = models.SlugField(unique=True, help_text=_("Unique identifier for URLs"))
    name = models.CharField(
        max_length=50,
        # choices=CATEGORY,
        # default=CATEGORY[0][0],
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
    # subcategory_list = models.ManyToManyField(
    #     SubCategory,
    #     blank=True,
    #     through='TypeFlowModel',  # ← Явно указываем модель
    #     related_name='categories'
    # )

    # subcategory_id = models.ForeignKey(
    #     SubCategory,
    #     on_delete=models.CASCADE,
    #     related_name="subcategories",
    #     verbose_name=_("SubCategory"),
    # )
    # subcategory_id = models.ManyToManyField(
    #     SubCategory,
    #     # through='Membership',
    #     related_name="subcategories",
    #     # verbose_name=_("SubCategory"),
    #
    # )
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

    def clean(self):
        super().clean()
        # self.validate_unique_subcategory()

    # def validate_unique_subcategory(self):
    #
    #     subcategory_list = CategoryModel.objects.exclude(id=self.id).filter(
    #         subcategory_id=self.subcategory_id.id
    #     )
    #     if len(subcategory_list) > 0:
    #         raise ValidationError(
    #             {
    #                 "subcategory_id": _(
    #                     'Subcategory "%(subcategory)s" is already used in category "%(category)s".'
    #                 )
    #                 % {
    #                     "subcategory": self.subcategory_id,
    #                     "category": CategoryModel.objects.get(
    #                         subcategory_id=self.subcategory_id.id
    #                     ),
    #                 }
    #             }
    #         )

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.slug = self.slug.lower()
        super().save(*args, **kwargs)


#
# class CategorySubcategory(models.Model):
#     category = models.ForeignKey(
#         CategoryModel, on_delete=models.CASCADE, related_name="Category"
#     )
#     subcategory = models.ForeignKey(
#         "SubCategory", on_delete=models.CASCADE, related_name="Subcategory"
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
