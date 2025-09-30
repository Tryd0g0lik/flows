"""
models_views/content_flow.py
"""

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
        validators=[MinValueValidator(1), MinValueValidator(300000)],
        help_text=_("Sum from 1 before 300000"),
    )
    comment = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        validators=[
            MaxLengthValidator(100),
            RegexValidator(
                regex="(^[A-Za-z][A-Za-z_ .,]{1,150}$)",
            ),
        ],
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Flow")
        verbose_name_plural = _("Flow")
        unique_together = ["slug"]

    def get_absolute_url(self):
        return f"/flow/{self.pk}/"
