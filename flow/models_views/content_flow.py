"""
models_views/content_flow.py
"""

from datetime import datetime

from django.core.validators import MinValueValidator, MaxLengthValidator, RegexValidator
from django.db import models

from django.utils.translation import gettext_lazy as _

from flow.models import InitialModel
from flow.models_views.status import StatusModel
from flow.models_views.types import TypeFlowModel


class ContentFlowsModel(InitialModel):
    """
    This is model for basic of flow's lines
    """

    type_id = models.ForeignKey(
        TypeFlowModel,
        on_delete=models.CASCADE,
        verbose_name=_("Type"),
        help_text=_("Select type name"),
    )

    status_id = models.ForeignKey(
        StatusModel,
        on_delete=models.CASCADE,
        verbose_name=_("Status"),
        help_text=_("Select status name"),
    )
    money = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
        ],
        help_text=_("Sum from 1 before 300000"),
    )
    comment = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Comments"),
        validators=[
            MaxLengthValidator(100),
            RegexValidator(
                regex="(^[A-Za-z][A-Za-z_ .,]{1,150}$)",
            ),
        ],
    )
    created_at = models.DateField(
        default=datetime.now, verbose_name=_("Date of creation"), null=True, blank=True
    )
    updated_at = models.DateField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Flow")
        verbose_name_plural = _("Flow")
        unique_together = ["slug"]

    def __str__(self):
        return self.type_id.name

    def get_absolute_url(self):
        return f"/flow/{self.pk}/"

    def save(self, *args, **kwargs):
        self.slug = self.slug.lower().replace(r" ", "_").replace("-", "_")
        super().save(*args, **kwargs)
