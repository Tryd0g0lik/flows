"""
models_views/status.py
"""

from django.db import models

# Create your models_views here.
from django.core import validators
from django.utils.translation import gettext_lazy as _

from project.settings import STATUS_OF_FLOW


class StatusModel(models.Model):
    name = models.CharField(
        max_length=50,
        # choices=STATUS_OF_FLOW,
        # default=STATUS_OF_FLOW[0][0],
        help_text="50 is MAX length of name.",
        verbose_name=_("Status name"),
        unique=True,
        validators=[
            validators.RegexValidator(
                regex="(^[A-Za-z][A-Za-z0-9_]{1,50}$)",
                message="Check valid a name.",
            ),
            validators.MaxLengthValidator(50),
        ],
    )

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")
        ordering = ("-name",)

    def __str__(self):
        return self.name
